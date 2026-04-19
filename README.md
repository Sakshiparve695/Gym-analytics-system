# 🏋️ Gym Data Pipeline & Analytics System

## 📌 Overview
This project is an end-to-end Data Engineering and analytics system that processes gym member activity data and generates insights using ETL pipelines.

It simulates how user activity data is collected, transformed, and used for analytics such as churn prediction and performance tracking.

---

## ⚙️ Tech Stack
- Python  
- FastAPI (REST API)  
- MySQL  
- Pandas  
- Scikit-learn  
- Docker  

---

## 🔄 Workflow

1. Member and attendance data is collected via API  
2. Data is stored in MySQL database  
3. ETL pipeline processes attendance data  
4. Data is transformed (visit counts, churn logic)  
5. Processed data is stored in analytics table  
6. APIs provide insights and predictions  

---

## 🧠 Data Architecture

- Raw Layer → Member & attendance data (MySQL)  
- Processed Layer → Aggregated visit data  
- Analytics Layer → member_analytics table  

---

## 🔄 ETL Pipeline

- Extract: Attendance data from database  
- Transform:  
  - Calculate total visits  
  - Identify churn risk  
- Load: Store results in `member_analytics` table  

---

## 📊 Features

- End-to-end ETL pipeline  
- Member activity tracking  
- Churn prediction using Logistic Regression  
- Data aggregation and analytics APIs  
- Visualization of attendance data  
- Containerized using Docker  

---

## 📁 Project Structure

gym_analytics/  
│── Gym_Management_System.py   # FastAPI backend  
│── etl.py                    # ETL pipeline  
│── requirements.txt  
│── Dockerfile  

---

## 📊 Key Functionalities

- Add, update, and manage members  
- Track attendance data  
- Identify high-risk (churn) members  
- Generate insights on user activity  
- Provide analytics via APIs  

---

## 💡 Key Learnings

- Built ETL pipeline for user activity data  
- Applied data transformation for analytics  
- Implemented basic machine learning for churn prediction  
- Integrated backend APIs with data workflows  
- Understood how data pipelines support business insights  

---

## 👩‍💻 Author

Sakshi Parve  
Aspiring Data Engineer | Python | SQL | ETL | GCP
