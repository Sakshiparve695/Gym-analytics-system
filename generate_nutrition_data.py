import mysql.connector
import random
from dotenv import load_dotenv
import os

load_dotenv()

# --------------------------------------------------
# Reproducible synthetic data
# --------------------------------------------------

random.seed(42)

# --------------------------------------------------
# Database Connection
# --------------------------------------------------

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

# --------------------------------------------------
# Fetch Existing Members
# --------------------------------------------------

cursor.execute("""
    SELECT member_id, age
    FROM members
""")

members = cursor.fetchall()

print(f"Members found: {len(members)}")

if not members:
    print("No members found. Exiting.")
    cursor.close()
    conn.close()
    exit()

# --------------------------------------------------
# Synthetic Nutrition Options
# --------------------------------------------------

goals = [
    "fat_loss",
    "maintenance",
    "muscle_gain"
]

diet_types = [
    "vegetarian",
    "vegan",
    "non_vegetarian"
]

# --------------------------------------------------
# Generate Nutrition Profiles
# --------------------------------------------------

nutrition_profiles = []

for member_id, age in members:

    # Generate a plausible synthetic height
    height_cm = round(random.uniform(150, 190), 2)

    # Generate a synthetic BMI-like range
    # Used only to keep demo data internally consistent
    bmi = random.uniform(19, 29)

    # Calculate weight from height and BMI
    height_m = height_cm / 100
    weight_kg = round(bmi * (height_m ** 2), 2)

    goal = random.choice(goals)
    diet_type = random.choice(diet_types)

    nutrition_profiles.append(
        (
            member_id,
            height_cm,
            weight_kg,
            goal,
            diet_type
        )
    )

# --------------------------------------------------
# Insert Nutrition Profiles
# --------------------------------------------------

cursor.executemany("""
    INSERT INTO member_diet_profile
    (
        member_id,
        height_cm,
        weight_kg,
        goal,
        diet_type
    )
    VALUES (%s, %s, %s, %s, %s)
""", nutrition_profiles)

conn.commit()

# --------------------------------------------------
# Summary
# --------------------------------------------------

print("=" * 50)
print("Nutrition Profiles Generated Successfully")
print(f"Profiles Inserted : {len(nutrition_profiles)}")
print("=" * 50)

cursor.close()
conn.close()