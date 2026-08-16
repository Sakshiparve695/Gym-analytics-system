from fastapi import FastAPI, HTTPException
import mysql.connector
import pandas as pd
from sklearn.linear_model import LogisticRegression
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import datetime

load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Gym Management API is running 🚀"}

from nutrition_recommender import (
    get_member_profile,
    get_member_attendance,
    get_activity_level,
    calculate_nutrition_target,
    get_foods,
    ml_recommend_meals,
    build_daily_plan
)
# -------- DB CONNECTION --------
def get_connection():
    return mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# -------- ADD MEMBER --------
@app.post("/members")
def add_member(name: str, age: int, phone: str, email: str, plan: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO members(name, age, phone, email, plan) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query, (name, age, phone, email, plan))
        conn.commit()

        cursor.close()
        conn.close()

        return {"message": "Member added successfully"}

    except mysql.connector.Error as err:
        if err.errno == 1062:
            return {"error": "Email already exists"}
        raise HTTPException(status_code=500, detail=str(err))


# -------- VIEW MEMBERS (FIXED CLEAN VERSION) --------
@app.get("/members")
def view_members():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM members")
        rows = cursor.fetchall()

        members = []
        for row in rows:
            members.append({
                "member_id": row[0],
                "name": row[1],
                "age": row[2],
                "phone": row[3],
                "email": row[4],
                "plan": row[5]
            })

        cursor.close()
        conn.close()

        return {"members": members}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------- MARK ATTENDANCE (RAW LAYER) --------
@app.post("/attendance")
def mark_attendance(member_id: int, visit_date: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO raw_attendance(member_id, visit_date) VALUES (%s,%s)"
        cursor.execute(query, (member_id, visit_date))
        conn.commit()

        cursor.close()
        conn.close()

        return {"message": "Attendance recorded in RAW layer"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------- ANALYTICS --------
@app.get("/analytics")
def get_analytics():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM member_analytics")
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return {"analytics": data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------- CHURN PREDICTION --------
@app.get("/churn")
def churn_prediction():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT member_id, total_visits, last_visit
        FROM member_analytics
        """)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        data = []
        today = datetime.date.today()

        for row in rows:
            member_id, visits, last_visit = row

            days_since_last = (today - last_visit).days if last_visit else 0
            avg_visits = visits / 4

            churn = 1 if visits < 5 or days_since_last > 10 else 0

            data.append([member_id, visits, avg_visits, days_since_last, churn])

        df = pd.DataFrame(data, columns=[
            "member_id", "visits", "avg_visits", "days_since_last", "churn"
        ])

        X = df[["visits", "avg_visits", "days_since_last"]]
        y = df["churn"]

        if len(set(y)) < 2:
            return {"message": "Not enough data"}

        model = LogisticRegression()
        model.fit(X, y)

        df["prediction"] = model.predict(X)

        result = []
        for _, row in df.iterrows():
            result.append({
                "member_id": int(row["member_id"]),
                "risk": "HIGH" if row["prediction"] == 1 else "LOW"
            })

        return {"churn_analysis": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------AI/ML Nutrition Recommendation---------
@app.get("/nutrition/recommendation/{member_id}")
def nutrition_recommendation(member_id: int):

    profile = get_member_profile(member_id)

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    visits = get_member_attendance(member_id)

    activity_level = get_activity_level(visits)

    nutrition_target = calculate_nutrition_target(
        profile,
        activity_level
    )

    foods = get_foods(profile["diet_type"])

    if not foods:
        raise HTTPException(
            status_code=404,
            detail="No meals available for this diet type"
        )

    ml_recommendations = ml_recommend_meals(
        foods,
        nutrition_target
    )

    daily_plan = build_daily_plan(
        foods,
        nutrition_target
    )

    total_calories = 0
    total_protein = 0
    plan = {}

    for meal_type, (meal, portion) in daily_plan.items():

        calories = float(meal["calories"]) * portion
        protein = float(meal["protein_g"]) * portion

        total_calories += calories
        total_protein += protein

        plan[meal_type] = {
            "food_name": meal["food_name"],
            "portion": portion,
            "calories": round(calories),
            "protein_g": round(protein)
        }

    return {
        "member_id": member_id,
        "goal": profile["goal"],
        "diet_type": profile["diet_type"],
        "activity_level": activity_level,
        "total_visits": visits,
        "nutrition_target": nutrition_target,
        "daily_plan": plan,
        "daily_total": {
            "calories": round(total_calories),
            "protein_g": round(total_protein)
        },
        "ml_recommendations": [
            {
                "food_name": meal["food_name"],
                "meal_type": meal["meal_type"],
                "calories": float(meal["calories"]),
                "protein_g": float(meal["protein_g"]),
                "distance": meal["similarity_distance"]
            }
            for meal in ml_recommendations
        ]
    }