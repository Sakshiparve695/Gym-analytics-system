import os
import time
import logging
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
# -------- DB CONNECTION FUNCTION --------
def get_connection():

    MAX_RETRIES = 10
    RETRY_DELAY = 5

    for attempt in range(MAX_RETRIES):
        try:
            logging.info(f"Attempt {attempt + 1} to connect to MySQL")

            conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                port=int(os.getenv("DB_PORT")),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
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
