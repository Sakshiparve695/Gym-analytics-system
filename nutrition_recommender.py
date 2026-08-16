import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


def get_member_profile(member_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            m.member_id,
            m.age,
            dp.height_cm,
            dp.weight_kg,
            dp.goal,
            dp.diet_type
        FROM members m
        JOIN member_diet_profile dp
            ON m.member_id = dp.member_id
        WHERE m.member_id = %s
    """, (member_id,))

    profile = cursor.fetchone()

    cursor.close()
    conn.close()

    return profile


def get_member_attendance(member_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM raw_attendance
        WHERE member_id = %s
    """, (member_id,))

    total_visits = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total_visits

def get_activity_level(total_visits):

    if total_visits >= 55:
        return "highly_active"

    elif total_visits >= 30:
        return "active"

    elif total_visits >= 10:
        return "moderately_active"

    else:
        return "low_activity"

def calculate_nutrition_target(profile, activity_level):

    age = profile["age"]
    height_cm = float(profile["height_cm"])
    weight_kg = float(profile["weight_kg"])
    goal = profile["goal"]

    # Mifflin-St Jeor baseline.
    # Sex is intentionally not stored in our current profile,
    # so we use a neutral portfolio-demo baseline.
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age)

    activity_multipliers = {
        "low_activity": 1.2,
        "moderately_active": 1.375,
        "active": 1.55,
        "highly_active": 1.725
    }

    maintenance_calories = bmr * activity_multipliers[activity_level]

    if goal == "fat_loss":
        daily_calories = maintenance_calories - 300

    elif goal == "muscle_gain":
        daily_calories = maintenance_calories + 250

    else:
        daily_calories = maintenance_calories

    protein_g = weight_kg * 1.6

    return {
        "daily_calories": round(daily_calories),
        "protein_g": round(protein_g)
    }
def get_foods(diet_type):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT food_id, food_name, meal_type,
               calories, protein_g, carbs_g, fat_g
        FROM nutrition_foods
        WHERE diet_type = %s
    """, (diet_type,))

    foods = cursor.fetchall()

    cursor.close()
    conn.close()

    return foods
def recommend_meals(foods, target):
    recommendations = {}

    for meal_type in ["breakfast", "lunch", "snack", "dinner"]:

        options = [
            food for food in foods
            if food["meal_type"] == meal_type
        ]

        if not options:
            continue

        # Target a simple calorie distribution
        calorie_targets = {
            "breakfast": target["daily_calories"] * 0.20,
            "lunch": target["daily_calories"] * 0.35,
            "snack": target["daily_calories"] * 0.15,
            "dinner": target["daily_calories"] * 0.30
        }

        target_calories = calorie_targets[meal_type]

        best_meal = min(
            options,
            key=lambda food: abs(
                float(food["calories"]) - target_calories
            )
        )

        recommendations[meal_type] = best_meal

    return recommendations
def ml_recommend_meals(foods, target):
    if not foods:
        return {}

    df = pd.DataFrame(foods)

    features = [
        "calories",
        "protein_g",
        "carbs_g",
        "fat_g"
    ]

    X = df[features].astype(float)

    # Scale nutrition features so calories don't dominate
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create target nutrition profile
    target_vector = [[
        target["daily_calories"] / 4,
        target["protein_g"] / 4,
        target["protein_g"] / 4,
        target["protein_g"] / 9
    ]]

    target_df = pd.DataFrame(target_vector, columns=features)
    target_scaled = scaler.transform(target_df)

    model = NearestNeighbors(
        n_neighbors=min(5, len(df)),
        metric="euclidean"
    )

    model.fit(X_scaled)

    distances, indices = model.kneighbors(target_scaled)

    recommendations = []

    for index, distance in zip(indices[0], distances[0]):
        meal = df.iloc[index].to_dict()
        meal["similarity_distance"] = round(float(distance), 4)
        recommendations.append(meal)

    return recommendations

def build_daily_plan(foods, target):

    meal_types = ["breakfast", "lunch", "snack", "dinner"]

    options = {}

    for meal_type in meal_types:
        options[meal_type] = [
            food for food in foods
            if food["meal_type"] == meal_type
        ]

    if any(not options[m] for m in meal_types):
        return {}

    best_plan = None
    best_score = float("inf")

    # Try portion sizes from 1.0x to 2.0x
    portions = [1.0, 1.25, 1.5, 1.75, 2.0]

    calorie_target = target["daily_calories"]
    protein_target = target["protein_g"]

    for breakfast in options["breakfast"]:
        for lunch in options["lunch"]:
            for snack in options["snack"]:
                for dinner in options["dinner"]:

                    meals = [breakfast, lunch, snack, dinner]

                    for portion in portions:

                        total_calories = sum(
                            float(meal["calories"]) * portion
                            for meal in meals
                        )

                        total_protein = sum(
                            float(meal["protein_g"]) * portion
                            for meal in meals
                        )

                        calorie_error = abs(
                            total_calories - calorie_target
                        )

                        protein_error = abs(
                            total_protein - protein_target
                        )

                        score = calorie_error + (protein_error * 10)

                        if score < best_score:
                            best_score = score

                            best_plan = {
                                "breakfast": (
                                    breakfast, portion
                                ),
                                "lunch": (
                                    lunch, portion
                                ),
                                "snack": (
                                    snack, portion
                                ),
                                "dinner": (
                                    dinner, portion
                                )
                            }

    return best_plan
if __name__ == "__main__":

    member_id = 1

    # Get member profile
    profile = get_member_profile(member_id)

    # Get attendance
    visits = get_member_attendance(member_id)

    # Determine activity level
    activity_level = get_activity_level(visits)

    # Calculate nutrition target
    nutrition_target = calculate_nutrition_target(
        profile,
        activity_level
    )

    # Get meals matching member's diet type
    foods = get_foods(profile["diet_type"])

    # ML Recommendations
    ml_recommendations = ml_recommend_meals(
        foods,
        nutrition_target
    )

    # Daily Meal Plan
    daily_plan = build_daily_plan(
        foods,
        nutrition_target
    )

    # Display Member Information
    print("=" * 50)
    print("GYMPULSE NUTRITION PROFILE")
    print("=" * 50)

    print("Profile:", profile)
    print("Total Visits:", visits)
    print("Activity Level:", activity_level)
    print("Nutrition Target:", nutrition_target)
    print("Available Meals:", len(foods))

    # Display ML Recommendations
    print("\nML Recommended Meals:")

    for meal in ml_recommendations:
        print(
            meal["food_name"],
            "|",
            meal["calories"],
            "kcal |",
            meal["protein_g"],
            "g protein |",
            "distance:",
            meal["similarity_distance"]
        )

    # Display Daily Plan
    print("\nDaily Nutrition Plan:")

    total_calories = 0
    total_protein = 0

    for meal_type, (meal, portion) in daily_plan.items():

        calories = float(meal["calories"]) * portion
        protein = float(meal["protein_g"]) * portion

        total_calories += calories
        total_protein += protein

        print(
            meal_type,
            "→",
            meal["food_name"],
            f"| Portion: {portion}x",
            f"| {round(calories)} kcal",
            f"| {round(protein)} g protein"
        )

    # Daily Totals
    print("\nDaily Plan Total:")
    print("Calories:", round(total_calories))
    print("Protein:", round(total_protein), "g")