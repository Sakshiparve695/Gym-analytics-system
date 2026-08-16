import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

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
# Nutrition Catalog
# --------------------------------------------------
# Values are synthetic/demo values for the portfolio
# and are intended for general fitness recommendations.

foods = [

    # -------------------------
    # BREAKFAST
    # -------------------------

    ("Oats + Milk + Banana", "breakfast", "vegetarian", 380, 15, 62, 9),
    ("Vegetable Poha + Curd", "breakfast", "vegetarian", 320, 11, 48, 9),
    ("Paneer Sandwich", "breakfast", "vegetarian", 410, 22, 42, 16),
    ("Moong Dal Chilla", "breakfast", "vegetarian", 300, 18, 38, 8),
    ("Greek Yogurt + Fruit", "breakfast", "vegetarian", 250, 18, 30, 6),
    ("Besan Chilla + Curd", "breakfast", "vegetarian", 330, 19, 40, 9),
    ("Vegetable Upma", "breakfast", "vegetarian", 310, 10, 48, 9),
    ("Peanut Butter Toast + Milk", "breakfast", "vegetarian", 420, 18, 45, 18),

    ("Tofu Scramble + Toast", "breakfast", "vegan", 350, 20, 38, 13),
    ("Overnight Oats + Soy Milk", "breakfast", "vegan", 360, 16, 55, 10),
    ("Chickpea Breakfast Bowl", "breakfast", "vegan", 370, 17, 54, 9),
    ("Peanut Butter Banana Toast", "breakfast", "vegan", 390, 14, 52, 15),

    ("Egg + Vegetable Toast", "breakfast", "non_vegetarian", 330, 21, 30, 13),
    ("Egg Oats Bowl", "breakfast", "non_vegetarian", 390, 24, 45, 12),
    ("Chicken Breakfast Wrap", "breakfast", "non_vegetarian", 420, 32, 40, 13),

    # -------------------------
    # LUNCH
    # -------------------------

    ("Dal + Rice + Salad", "lunch", "vegetarian", 520, 20, 78, 12),
    ("Paneer Rice Bowl", "lunch", "vegetarian", 560, 28, 65, 18),
    ("Rajma Rice + Salad", "lunch", "vegetarian", 510, 21, 76, 9),
    ("Chole + Roti + Salad", "lunch", "vegetarian", 500, 19, 70, 12),
    ("Paneer Roti Bowl", "lunch", "vegetarian", 540, 30, 58, 19),
    ("Vegetable Khichdi + Curd", "lunch", "vegetarian", 480, 18, 68, 12),
    ("Tofu Rice Bowl", "lunch", "vegetarian", 510, 27, 62, 15),
    ("Dal + Roti + Vegetables", "lunch", "vegetarian", 490, 19, 66, 13),

    ("Tofu Quinoa Bowl", "lunch", "vegan", 500, 25, 65, 15),
    ("Chickpea Rice Bowl", "lunch", "vegan", 520, 20, 80, 10),
    ("Rajma Quinoa Bowl", "lunch", "vegan", 510, 22, 72, 11),
    ("Lentil Vegetable Bowl", "lunch", "vegan", 470, 24, 65, 9),

    ("Chicken Rice Bowl", "lunch", "non_vegetarian", 560, 42, 62, 15),
    ("Chicken Roti + Salad", "lunch", "non_vegetarian", 530, 40, 55, 14),
    ("Grilled Chicken Quinoa Bowl", "lunch", "non_vegetarian", 550, 45, 58, 13),
    ("Fish Rice + Vegetables", "lunch", "non_vegetarian", 520, 38, 60, 12),

    # -------------------------
    # SNACKS
    # -------------------------

    ("Greek Yogurt + Nuts", "snack", "vegetarian", 220, 15, 15, 11),
    ("Paneer Cubes + Fruit", "snack", "vegetarian", 240, 18, 20, 10),
    ("Milk + Banana", "snack", "vegetarian", 210, 9, 34, 5),
    ("Roasted Chana + Fruit", "snack", "vegetarian", 200, 10, 32, 4),
    ("Curd + Seeds", "snack", "vegetarian", 190, 12, 12, 10),
    ("Peanut Butter Toast", "snack", "vegetarian", 230, 9, 28, 10),

    ("Hummus + Vegetables", "snack", "vegan", 180, 7, 22, 8),
    ("Roasted Chickpeas", "snack", "vegan", 210, 10, 32, 5),
    ("Soy Yogurt + Fruit", "snack", "vegan", 190, 9, 25, 6),
    ("Peanut Butter Banana", "snack", "vegan", 240, 8, 30, 11),

    ("Boiled Eggs + Fruit", "snack", "non_vegetarian", 200, 13, 18, 9),
    ("Chicken Sandwich", "snack", "non_vegetarian", 290, 24, 28, 10),
    ("Egg + Toast", "snack", "non_vegetarian", 230, 15, 22, 9),

    # -------------------------
    # DINNER
    # -------------------------

    ("Paneer + Roti + Vegetables", "dinner", "vegetarian", 520, 30, 55, 18),
    ("Dal + Roti + Salad", "dinner", "vegetarian", 470, 19, 64, 12),
    ("Tofu + Rice + Vegetables", "dinner", "vegetarian", 500, 27, 62, 14),
    ("Paneer Vegetable Bowl", "dinner", "vegetarian", 480, 29, 42, 18),
    ("Khichdi + Curd", "dinner", "vegetarian", 450, 18, 62, 10),
    ("Chole + Roti", "dinner", "vegetarian", 480, 18, 67, 11),
    ("Soya Chunk Curry + Roti", "dinner", "vegetarian", 500, 32, 55, 12),

    ("Tofu Stir Fry + Rice", "dinner", "vegan", 490, 26, 65, 13),
    ("Lentil Curry + Rice", "dinner", "vegan", 480, 21, 72, 8),
    ("Chickpea Wrap", "dinner", "vegan", 450, 18, 62, 12),
    ("Tofu Vegetable Bowl", "dinner", "vegan", 430, 25, 40, 16),

    ("Grilled Chicken + Rice", "dinner", "non_vegetarian", 540, 43, 60, 13),
    ("Chicken Roti + Vegetables", "dinner", "non_vegetarian", 510, 40, 52, 14),
    ("Grilled Fish + Rice", "dinner", "non_vegetarian", 500, 38, 58, 11),
    ("Chicken Quinoa Bowl", "dinner", "non_vegetarian", 530, 44, 55, 13),
]

# --------------------------------------------------
# Insert Catalog
# --------------------------------------------------

cursor.executemany("""
    INSERT INTO nutrition_foods
    (
        food_name,
        meal_type,
        diet_type,
        calories,
        protein_g,
        carbs_g,
        fat_g
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", foods)

conn.commit()

# --------------------------------------------------
# Summary
# --------------------------------------------------

print("=" * 50)
print("Nutrition Food Catalog Generated Successfully")
print(f"Meals Inserted : {len(foods)}")
print("=" * 50)

cursor.close()
conn.close()