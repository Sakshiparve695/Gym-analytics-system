# 🚀 GymPulse Analytics Platform
### End-to-End Gym Management & Data Analytics Solution using FastAPI, MySQL, ETL, PySpark, Databricks, Machine Learning, Power BI & GitHub Actions


---

# 🚀 Project Overview

GymPulse Analytics Platform is an end-to-end data engineering and analytics project that simulates a modern gym management and analytics system. It combines REST APIs, MySQL, Python ETL, dimensional data modeling, PySpark analytics, Databricks, machine learning-based nutrition recommendations, Power BI dashboards and GitHub Actions CI/CD.

The platform automates the journey of gym data from member and attendance management through data transformation, analytics and business intelligence reporting.


---

# 🎯 Business Problem

Gym management systems generate large volumes of member, membership and attendance data. Managing this information directly in operational tables makes analytical reporting difficult, repetitive and time-consuming.

There was a need for a centralized platform that could:

- Manage gym members and attendance through APIs
- Store operational data in MySQL
- Transform raw data into analytics-ready datasets
- Build dimensional data structures for reporting
- Analyze member activity and membership performance
- Generate attendance and membership insights
- Provide nutrition recommendations based on member profiles and activity
- Present business insights through Power BI dashboards
- Automate code validation using CI/CD


---

# 🎯 Solution

GymPulse was designed as a layered data analytics platform.

Member and attendance information is managed through FastAPI and stored in MySQL. Python-based ETL processes transform operational data into structured analytical datasets. Dimensional datasets such as members, plans and dates are generated for analytics.

PySpark and Databricks are used for scalable data processing and analytical transformations. Machine learning is used in the nutrition recommendation module to identify meals based on nutritional similarity. Power BI provides interactive dashboards for attendance, membership and nutrition analytics.

GitHub Actions provides automated CI/CD validation for the project.


---

# 🏗️ GymPulse Analytics Platform
### End-to-End Gym Management & Data Analytics Architecture

```text
                                      ┌──────────────────────┐
                                      │      Client/User     │
                                      └──────────┬───────────┘
                                                 │
                                                 ▼
                                   ┌─────────────────────────┐
                                   │      FastAPI REST API   │
                                   │   Gym Management System │
                                   └──────────┬──────────────┘
                                              │
                           Add / Update / Fetch Members & Attendance
                                              │
                                              ▼
                                   ┌─────────────────────────┐
                                   │      MySQL Database     │
                                   │   Operational / Raw Data │
                                   └──────────┬──────────────┘
                                              │
                                              ▼
                              ┌────────────────────────────────┐
                              │        Python ETL Pipeline     │
                              │--------------------------------│
                              │ • Extract Raw Data             │
                              │ • Data Validation              │
                              │ • Data Cleaning                │
                              │ • Data Transformation          │
                              │ • Generate Analytics Datasets  │
                              └──────────┬─────────────────────┘
                                         │
                                         ▼
                              ┌───────────────────────────────┐
                              │     Dimensional Data Layer    │
                              │-------------------------------│
                              │ • dim_member                   │
                              │ • dim_plan                     │
                              │ • dim_date                     │
                              │ • fact_attendance               │
                              │ • member_analytics              │
                              └──────────┬────────────────────┘
                                         │
                          ┌──────────────┴──────────────┐
                          ▼                             ▼
               ┌──────────────────────┐      ┌────────────────────────┐
               │   PySpark Analytics  │      │ Databricks Analytics   │
               │ • Transformations    │      │ • Data Processing      │
               │ • Aggregations       │      │ • Analytics Jobs       │
               │ • Data Analysis      │      │ • Scheduled Workflows  │
               └──────────┬───────────┘      └───────────┬────────────┘
                          │                              │
                          └──────────────┬───────────────┘
                                         ▼
                              ┌───────────────────────────┐
                              │      Power BI Dashboards  │
                              │---------------------------│
                              │ • Attendance Analytics    │
                              │ • Membership Analytics    │
                              │ • Nutrition Analytics     │
                              │ • Member Insights         │
                              └───────────────────────────┘

                    ┌─────────────────────────────────────┐
                    │     Machine Learning Module         │
                    │ Nutrition Recommendation System    │
                    │ • Member Profile                    │
                    │ • Activity Level                    │
                    │ • Calorie / Protein Target          │
                    │ • Meal Similarity Recommendation    │
                    └─────────────────────────────────────┘

                    ┌─────────────────────────────────────┐
                    │       GitHub Actions CI/CD          │
                    │ • Python Validation                  │
                    │ • FastAPI Validation                 │
                    │ • ML Module Validation               │
                    │ • Docker Compose Validation          │
                    │ • Container Build                    │
                    └─────────────────────────────────────┘
```


---

# Data Flow

1. Member and attendance information is submitted through FastAPI REST APIs.
2. Operational records are stored in MySQL.
3. Python ETL processes extract, validate, clean and transform raw data.
4. Structured dimensional datasets are generated for analytical workloads.
5. Attendance, membership and member analytics datasets are prepared for reporting.
6. PySpark performs analytical transformations and aggregations.
7. Databricks executes analytics workloads and scheduled jobs.
8. The nutrition recommendation module retrieves member profile and attendance information.
9. Machine learning identifies nutritionally similar meal options.
10. Power BI provides interactive dashboards for business analysis.
11. GitHub Actions automatically validates the application and Docker configuration on code changes.


---

# ⚙️ Technology Stack

| Category | Technologies |
|-----------|--------------|
| **Programming Language** | Python 3.11 |
| **Backend Framework** | FastAPI |
| **Operational Database (OLTP)** | MySQL |
| **Data Ingestion** | REST APIs, JSON |
| **ETL Pipeline** | Python, Pandas |
| **Data Modeling** | Dimensional Data Model |
| **Data Processing** | PySpark |
| **Big Data Platform** | Databricks |
| **Machine Learning** | Scikit-learn |
| **ML Technique** | Nearest Neighbors, StandardScaler |
| **Business Intelligence** | Microsoft Power BI |
| **Containerization** | Docker, Docker Compose |
| **CI/CD** | GitHub Actions |
| **Version Control** | Git, GitHub |
| **Development Tools** | VS Code |
| **Database Connectivity** | mysql-connector-python |
| **Configuration** | python-dotenv |


---

# 🔄 End-to-End Data Engineering & Analytics Pipeline

GymPulse follows a layered architecture that transforms operational gym management data into analytics-ready datasets, dashboards and intelligent recommendations.


---

## 📥 Step 1 — Data Ingestion Layer

Gym member and attendance information is managed through FastAPI REST APIs.

The API acts as the entry point for gym management operations.

### Data handled by the platform

- Member Information
- Membership Plans
- Attendance Records
- Member Analytics
- Nutrition Profiles

Example API interaction:

```text
FastAPI REST API
        ↓
Member / Attendance Request
        ↓
MySQL Database
```


---

## 🗄️ Step 2 — Operational Database (MySQL)

The application uses MySQL as the operational database for storing gym management data.

The project contains tables supporting members, plans, attendance, nutrition profiles and analytical processing.

Examples include:

```sql
members
plans
member_plan
raw_attendance
stg_attendance
attendance
member_analytics
member_diet_profile
nutrition_foods
```

The operational layer stores the data required by the API and downstream analytics processes.


---

## 🔄 Step 3 — ETL Processing

A Python-based ETL pipeline transforms operational data into structured analytical datasets.

### ETL Operations

- Extract Raw Records
- Data Validation
- Data Cleaning
- Data Transformation
- Attendance Processing
- Dimension Generation
- Fact Data Generation
- Analytics Dataset Preparation
- Logging & Error Handling

The ETL process prepares data for analytical workloads instead of directly querying operational data for every report.


---

## 📂 Step 4 — Dimensional Data Layer

GymPulse uses structured dimensional datasets for analytical reporting.

### Generated Dimensions

```text
dim_member
dim_plan
dim_date
```

### Fact Dataset

```text
fact_attendance
```

### Analytical Dataset

```text
member_analytics
```

This structure provides organized analytical data for attendance and membership reporting.


---

## 📊 Step 5 — Attendance & Membership Analytics

The analytical layer supports insights into gym activity and membership performance.

### Analytics include

- Attendance trends
- Most active members
- Membership performance
- Member activity
- Plan-level analysis
- Member analytics
- Attendance summaries

These datasets are used as inputs for Power BI reporting and further analytical processing.


---

## ⚡ Step 6 — PySpark Analytics Layer

PySpark is used for data processing and analytical transformations.

### Implemented Areas

- Spark version validation
- DataFrame processing
- Dataset transformations
- Analytical aggregations
- Data preparation
- Large-scale data processing

PySpark provides a scalable analytics layer for the GymPulse platform.


---

## ☁️ Step 7 — Databricks Analytics Layer

Databricks is used as the cloud analytics environment for the project.

### Implemented Features

- Databricks workspace
- Spark-based analytics
- Unity Catalog usage
- Analytics tables
- Data loading
- Scheduled analytics job
- Job execution monitoring

The project includes evidence of successful Databricks job execution and analytics processing.


---

## 🤖 Step 8 — Machine Learning Nutrition Recommendation

GymPulse includes a machine learning-based nutrition recommendation module.

The module retrieves a member's profile and attendance information from MySQL and determines an activity level based on total visits.

The nutrition target is calculated using member age, height, weight, goal and activity level.

### Nutrition Target

The system calculates:

- Daily calorie target
- Daily protein target
- Activity level

The system supports goals such as:

- Fat Loss
- Muscle Gain
- Maintenance


### Machine Learning Recommendation

The nutrition recommender uses:

```text
StandardScaler
NearestNeighbors
```

Nutrition features include:

```text
Calories
Protein
Carbohydrates
Fat
```

The features are scaled before similarity calculation so that calories do not dominate the recommendation.

The model identifies nutritionally similar food options and produces meal recommendations.


---

## 🍽️ Step 9 — Daily Nutrition Planning

The nutrition module also builds a daily meal plan.

Meal categories include:

- Breakfast
- Lunch
- Snack
- Dinner

The system evaluates different food combinations and portion sizes against the member's calorie and protein targets.

The final plan attempts to minimize the difference between the target nutritional requirements and the generated meal plan.


---

## 📈 Step 10 — Business Intelligence (Power BI)

Power BI is used to visualize the analytical datasets generated by GymPulse.

### Dashboard Areas

- Attendance Dashboard
- Membership Analytics
- Nutritional Analysis
- Member Activity
- Most Active Members
- Attendance Trends

### Business Insights

- Monitor member attendance
- Identify active members
- Analyze membership plans
- Understand attendance patterns
- Analyze nutritional recommendations
- Support data-driven gym management decisions


---

# 🔌 REST API Endpoints

The FastAPI application provides endpoints for gym management and analytics functionality.

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/members` | Retrieve gym members |
| POST | `/members` | Create a new member |
| GET | `/members/{member_id}` | Retrieve a specific member |
| PUT | `/members/{member_id}` | Update member information |
| DELETE | `/members/{member_id}` | Delete a member |
| POST | `/attendance` | Add attendance record |
| GET | `/attendance` | Retrieve attendance records |
| GET | `/analytics/member/{member_id}` | Retrieve member analytics |
| GET | `/analytics/attendance` | Retrieve attendance analytics |
| GET | `/analytics/churn` | Retrieve churn analysis |
| GET | `/nutrition/recommend/{member_id}` | Generate nutrition recommendations |


---

# 📊 Analytics Delivered

The platform provides insights into:

- Member Attendance
- Attendance Trends
- Most Active Members
- Membership Plan Performance
- Member Analytics
- Attendance Statistics
- Nutrition Analysis
- Calorie Targets
- Protein Targets
- Meal Recommendations
- Churn Analysis
- Business KPIs


---

# ☁️ Databricks & Cloud Analytics

GymPulse includes a Databricks-based analytics environment for scalable data processing.

The project includes:

- Databricks Workspace
- Spark Processing
- Unity Catalog
- Analytics Tables
- Data Loading
- Scheduled Databricks Job
- Job Execution Monitoring

The project screenshots document the analytics workflow and successful job execution.


---

# ⚙️ CI/CD with GitHub Actions

GymPulse includes a GitHub Actions CI/CD pipeline that automatically validates the project whenever changes are pushed to the `main` branch or submitted through a pull request.

### CI/CD Pipeline

The workflow performs:

- Repository checkout
- Python 3.11 setup
- Dependency installation
- Python syntax validation
- FastAPI application validation
- Nutrition recommendation module validation
- Docker Compose configuration validation
- Docker container build

This provides automated quality checks before changes are considered ready.


---

# ⭐ Key Features

GymPulse Analytics Platform demonstrates an end-to-end gym management and data engineering workflow.

### Core Features

- 🏋️ FastAPI-based Gym Management System
- 👥 Member Management
- 📅 Attendance Management
- 🗄️ MySQL Operational Database
- 🔄 Python ETL Pipeline
- 📂 Dimensional Data Architecture
- 📊 Attendance & Membership Analytics
- ⚡ PySpark Analytics
- ☁️ Databricks Analytics Platform
- 🧠 Machine Learning Nutrition Recommendation
- 🍽️ Personalized Meal Recommendation
- 📈 Power BI Business Dashboards
- 🐳 Dockerized Environment
- ⚙️ GitHub Actions CI/CD
- 🔐 Secure Configuration using Environment Variables


---

# 🧩 Engineering Challenges Solved

Throughout the project, several engineering challenges were addressed while integrating backend development, data engineering, analytics, machine learning and business intelligence into a unified platform.

### Backend Engineering

- Designed REST APIs using FastAPI
- Implemented member management operations
- Implemented attendance management
- Connected FastAPI with MySQL
- Added analytics endpoints


### Data Engineering

- Designed structured analytical datasets
- Built ETL processing for attendance data
- Implemented data validation and transformation
- Generated dimensional datasets
- Created fact and analytical datasets
- Separated operational and analytical workloads


### Analytics Engineering

- Processed datasets using PySpark
- Built analytical transformations
- Generated member and attendance insights
- Used Databricks for scalable processing
- Implemented scheduled analytics execution


### Machine Learning

- Built a nutrition recommendation module
- Scaled nutritional features using StandardScaler
- Applied NearestNeighbors for similarity-based recommendations
- Calculated activity levels from attendance
- Generated calorie and protein targets
- Built daily meal recommendations


### Business Intelligence

- Built Power BI dashboards
- Created attendance analytics
- Created membership analytics
- Created nutrition analysis
- Developed member activity insights


### DevOps / CI/CD

- Created GitHub Actions workflow
- Automated dependency installation
- Added Python syntax validation
- Added FastAPI module validation
- Added ML module validation
- Added Docker Compose validation
- Added Docker build validation


---

# 📁 Project Structure

```text
GYM_Management_analytics/
│
├── Gym_Management_System.py          # FastAPI Gym Management API
├── etl.py                            # ETL Pipeline
├── generate_members.py               # Member Data Generator
├── Generate_Attendence.py            # Attendance Data Generator
├── generate_food_catalog.py          # Nutrition Food Catalog Generator
├── generate_nutrition_data.py        # Nutrition Data Generator
├── nutrition_recommender.py          # ML Nutrition Recommendation System
│
├── requirements.txt
├── .env.example
├── docker-compose.yml
│
├── Fact_attendence.csv
├── Nutrition_Analysis.csv
├── dim_date.csv
├── dim_member.csv
├── dim_plan.csv
├── fact_deliveries_File.csv
│
├── sakshi_project_db_attendance.sql
├── sakshi_project_db_dim_date.sql
├── sakshi_project_db_dim_member.sql
├── sakshi_project_db_dim_plan.sql
├── sakshi_project_db_fact_attendance.sql
├── sakshi_project_db_member_analytics.sql
├── sakshi_project_db_routines.sql
│
├── Screenshots/
│   ├── Attendance_Dashboard_PBI.png
│   ├── Azure_Databricks _Workspace.png
│   ├── Data_Loading.png
│   ├── Databricks_job_success.png
│   ├── Date_Dimension.png
│   ├── Joined_DataSET.png
│   ├── Member_Dimension.png
│   ├── Membership_Analytics.png
│   ├── Most_Active_Member.png
│   ├── Nutritional_Analysis_PBI.png
│   ├── PBI_Attendance_Dashboard.png
│   ├── Testing_endpoint_1.png
│   ├── Testing_endpoint_2.png
│   ├── Unity_Catlogue_Volume.png
│   ├── Warehouse_analytics_Table.png
│   ├── spark_Version.png
│   └── FastAPI_Attendence_Endpoint.png
│
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions CI/CD
│
└── README.md
```


---

# 🚀 Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Sakshiparve695/Gym-analytics-system.git
cd Gym-analytics-system
```


---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```


---

## 3️⃣ Configure Environment Variables

Create a `.env` file locally and configure your MySQL connection.

```env
DB_HOST=<your_host>
DB_PORT=3306
DB_USER=<your_username>
DB_PASSWORD=<your_password>
DB_NAME=sakshi_project_db
```

Do not commit the `.env` file to GitHub.

Use `.env.example` as the configuration template.


---

## 4️⃣ Start the REST API

```bash
uvicorn Gym_Management_System:app --reload
```

The FastAPI application will start locally and provide the interactive API documentation.


---

## 5️⃣ Execute ETL Pipeline

```bash
python etl.py
```


---

## 6️⃣ Generate Project Data

Member and attendance data can be generated using the project data-generation scripts.

```bash
python generate_members.py
python Generate_Attendence.py
```

Nutrition data can be generated using:

```bash
python generate_food_catalog.py
python generate_nutrition_data.py
```


---

## 7️⃣ Run the Nutrition Recommendation Module

```bash
python nutrition_recommender.py
```

The module retrieves member information, attendance, nutrition targets and available food data to generate machine learning-based meal recommendations.


---

## 8️⃣ Launch Docker Environment

```bash
docker compose up -d
```

Docker Compose can be used to run the project's containerized services.


---

## 9️⃣ Explore Databricks Analytics

Upload or connect the project analytics datasets to the Databricks environment and execute the PySpark analytics workflow.

The repository contains supporting SQL files, analytical datasets and screenshots documenting the Databricks workflow.


---

## 🔟 Open Power BI Dashboards

Open the Power BI reports and connect them to the prepared analytical datasets to explore:

- Attendance Analytics
- Membership Analytics
- Nutrition Analysis
- Member Activity


---

# 🚀 Future Roadmap

The GymPulse architecture can be extended with additional enterprise-grade capabilities.

Planned improvements include:

- 📡 Real-Time Attendance Streaming using Apache Kafka
- 📊 Advanced Data Quality Monitoring
- 📩 Email Notifications & Alerts
- 🤖 Advanced Predictive Member Churn
- 🧠 More Personalized Nutrition Recommendations
- 📈 Real-Time Power BI Dashboards
- 🏗️ Microsoft Fabric / Lakehouse Integration
- ☁️ Cloud Deployment of the Complete Analytics Platform
- 📦 Data Versioning & Lineage Tracking
- 🔐 Advanced Authentication and Role-Based Access Control


---

# 👩‍💻 Author

## Sakshi Parve

**Aspiring Data Engineer**

**Tech Stack**

Python • SQL • FastAPI • MySQL • PySpark • Databricks • Power BI • Docker • Git • GitHub • Machine Learning


---

⭐ If you found this project useful, consider giving it a Star.

