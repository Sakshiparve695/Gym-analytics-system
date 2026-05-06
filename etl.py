import mysql.connector
import logging
import os
import time
from dotenv import load_dotenv

load_dotenv()

# -------- LOGGING --------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------- DB CONNECTION FUNCTION --------
#def get_connection():
#    return mysql.connector.connect(
        #host = "localhost",
        #host = "host.docker.internal",
#        host="db",
#        user="root",
#        password=os.getenv("DB_PASSWORD"),
#        database="sakshi_project_db"
#    )
def get_connection():

    MAX_RETRIES = 10
    RETRY_DELAY = 5

    for attempt in range(MAX_RETRIES):
        try:
            logging.info(f"Attempt {attempt + 1} to connect to MySQL")

            conn = mysql.connector.connect(
                host="db",
                user="root",
                password=os.getenv("DB_PASSWORD"),
                database="sakshi_project_db"
            )

            logging.info("Connected to MySQL successfully")
            return conn

        except mysql.connector.Error as e:
            logging.error(f"MySQL Connection Failed: {e}")

            if attempt < MAX_RETRIES - 1:
                logging.info(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                logging.error("Max retries reached. Exiting.")
                raise

def run_etl():
    logging.info("ETL Started")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # -------- STEP 1: GET OR INIT METADATA --------
        cursor.execute("""
            SELECT last_run FROM etl_metadata
            WHERE job_name = 'attendance_etl'
        """)
        result = cursor.fetchone()

        if result is None:
            logging.warning("Metadata not found. Initializing...")
            last_run = "2000-01-01 00:00:00"

            cursor.execute("""
                INSERT INTO etl_metadata (job_name, last_run)
                VALUES ('attendance_etl', %s)
            """, (last_run,))
            conn.commit()
        else:
            last_run = result[0]

        # -------- STEP 2: EXTRACT FROM RAW --------
        cursor.execute("""
            SELECT member_id, visit_date, created_at
            FROM raw_attendance
            WHERE created_at > %s
        """, (last_run,))
        raw_rows = cursor.fetchall()

        if not raw_rows:
            logging.info("No new data to process")
            return

        logging.info(f"Processing {len(raw_rows)} new records")

        # -------- STEP 3: LOAD TO STAGING --------
        valid_rows = 0
        for member_id, visit_date, _ in raw_rows:
            if member_id is None or visit_date is None:
                continue

            cursor.execute("""
                INSERT INTO stg_attendance (member_id, visit_date)
                VALUES (%s, %s)
            """, (member_id, visit_date))
            valid_rows += 1

        conn.commit()
        logging.info(f"Inserted {valid_rows} records into staging")

        # -------- STEP 4: TRANSFORM --------
        cursor.execute("""
            SELECT member_id,
                   COUNT(*) AS visits,
                   MAX(visit_date) AS last_visit
            FROM stg_attendance
            GROUP BY member_id
        """)
        stg_data = cursor.fetchall()

        # -------- STEP 5: LOAD TO FACT --------
        for member_id, visits, last_visit in stg_data:
            cursor.execute("""
                INSERT INTO member_analytics (member_id, total_visits, last_visit)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    total_visits = total_visits + VALUES(total_visits),
                    last_visit = GREATEST(last_visit, VALUES(last_visit))
            """, (member_id, visits, last_visit))

        # -------- STEP 5.5: UPDATE CHURN --------
        cursor.execute("""
            UPDATE member_analytics
            SET churn_risk = CASE
                WHEN total_visits < 5 THEN 1
                ELSE 0
            END
        """)

        # -------- STEP 6: UPDATE METADATA --------
        cursor.execute("""
            UPDATE etl_metadata
            SET last_run = NOW()
            WHERE job_name = 'attendance_etl'
        """)

        conn.commit()

        # -------- STEP 7: CLEAN STAGING --------
        cursor.execute("TRUNCATE TABLE stg_attendance")
        conn.commit()

        logging.info("ETL Completed Successfully")

    except Exception as e:
        logging.error(f"ETL Failed: {str(e)}")

    finally:
        cursor.close()
        conn.close()


# -------- SCHEDULER --------
if __name__ == "__main__":
    while True:
        run_etl()
        time.sleep(300)  # every 5 mins