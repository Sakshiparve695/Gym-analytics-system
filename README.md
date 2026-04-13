# Gym Analytics System

## 🚀 Overview
A backend system built using FastAPI and MySQL to manage gym members, track attendance, and generate analytical insights. The system integrates ETL pipelines and Machine Learning to predict member churn and support data-driven decision-making.

---

## 🧠 System Architecture & Flow

1. **Data Ingestion (FastAPI)**
   - REST APIs collect data for members and attendance.
   - Endpoints like `/members` and `/attendance` handle real-time operations.

2. **Data Storage (MySQL)**
   - Raw operational data is stored in relational tables.
   - Tables include members, attendance, and users.

3. **ETL Pipeline**
   - Extracts attendance data.
   - Transforms it into analytical features (visits, recency, churn risk).
   - Loads processed data into `member_analytics` table.

4. **Machine Learning Layer**
   - Logistic Regression model predicts churn risk.
   - Uses behavioral features like frequency and recency.

5. **Analytics & Insights**
   - APIs like `/insights` and `/churn` provide business insights.
   - Heap-based optimization identifies top active members.

6. **Authentication Layer**
   - Secure access using signup and login APIs.

7. **Deployment (Docker)**
   - Application is containerized using Docker.
   - Ensures consistent environment and easy deployment.

---

## ⚙️ Features
- Member management (CRUD APIs)
- Attendance tracking
- Churn prediction (ML)
- ETL pipeline for analytics
- Top active members using Heap
- Authentication (Signup/Login)
- Dockerized deployment

---

## 🛠️ Tech Stack
- Python, FastAPI
- MySQL
- Pandas, Scikit-learn
- Docker
- REST APIs, ETL, Machine Learning

---

## ▶️ Run Locally
```bash
uvicorn Gym_Management_System:app --reload
---
🐳 Run with Docker
docker build -t gym-api .
docker run -p 8000:8000 -e DB_HOST=host.docker.internal gym-api
---

📊 API Documentation

Visit:
http://127.0.0.1:8000/docs

---

👩‍💻 Author

Sakshi Parve
