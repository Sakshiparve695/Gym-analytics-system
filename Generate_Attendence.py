import mysql.connector
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

# -----------------------------
# Database Connection
# -----------------------------
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

# -----------------------------
# Fetch Member IDs
# -----------------------------
cursor.execute("SELECT member_id FROM members")
member_ids = [row[0] for row in cursor.fetchall()]

random.shuffle(member_ids)

# -----------------------------
# Split Members
# -----------------------------
total = len(member_ids)

hardcore = member_ids[:int(total * 0.20)]
regular = member_ids[int(total * 0.20):int(total * 0.70)]
casual = member_ids[int(total * 0.70):int(total * 0.90)]
inactive = member_ids[int(total * 0.90):]

today = datetime.today()

attendance = []

# -----------------------------
# Attendance Generator
# -----------------------------
def generate(member_list, min_visits, max_visits):

    for member in member_list:

        visits = random.randint(min_visits, max_visits)

        used_dates = set()

        while len(used_dates) < visits:

            days_back = random.randint(0, 89)

            visit_date = (
                today - timedelta(days=days_back)
            ).date()

            if visit_date in used_dates:
                continue

            used_dates.add(visit_date)

            attendance.append(
                (
                    member,
                    visit_date
                )
            )

# -----------------------------
# Generate Attendance
# -----------------------------
generate(hardcore,55,75)
generate(regular,30,45)
generate(casual,10,20)
generate(inactive,1,5)

# -----------------------------
# Bulk Insert
# -----------------------------
cursor.executemany("""
INSERT INTO raw_attendance
(member_id,visit_date)
VALUES(%s,%s)
""", attendance)

conn.commit()

print("="*50)
print("Attendance Generated Successfully")
print(f"Rows Inserted : {len(attendance)}")
print("="*50)

cursor.close()
conn.close()