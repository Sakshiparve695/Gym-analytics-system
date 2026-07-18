import requests
import random

# -----------------------------
# Sample Data
# -----------------------------

first_names = [
    "Aarav","Vivaan","Aditya","Vihaan","Arjun","Krishna","Sai","Rohan","Rahul","Karan",
    "Ananya","Diya","Priya","Riya","Sneha","Aisha","Pooja","Sakshi","Meera","Ishita"
]

last_names = [
    "Sharma","Patel","Verma","Gupta","Singh","Joshi","Kulkarni",
    "Patil","Deshmukh","Parve"
]

plans = [1, 2, 3]

# -----------------------------
# Generate 100 Members
# -----------------------------

for i in range(1, 101):

    name = f"{random.choice(first_names)} {random.choice(last_names)}"

    age = random.randint(18, 60)

    phone = f"98{random.randint(10000000,99999999)}"

    email = f"member{i}@gympulse.com"

    payload = {
        "name": name,
        "age": age,
        "phone": phone,
        "email": email,
        "plan": random.choice(plans)
    }

    response = requests.post(
        "http://127.0.0.1:8000/members",
        params=payload
    )

    print(f"{i} -> {response.status_code} -> {response.json()}")