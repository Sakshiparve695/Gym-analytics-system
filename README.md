# 🏋️ Gym Data Pipeline System (ETL + Analytics + ML)

## 🚀 Overview

This project implements an end-to-end **data engineering pipeline** for fitness analytics. It ingests workout data via APIs, processes it through ETL pipelines, and generates insights for performance tracking and optimization.

---

## 🎯 Problem Statement

Fitness systems generate large volumes of workout data (user activity, duration, intensity), but this data is often not structured for analysis.

This system solves that by:

* Building a structured **data pipeline (raw → processed → fact)**
* Enabling analytics on user performance
* Supporting predictive insights using machine learning

---

## 🏗️ Architecture

```
Client / API Testing Tool
        │
        ▼
FastAPI (Data Ingestion Layer)
        │
        ▼
MySQL - Raw Layer (raw_gym_data)
        │
        ▼
ETL Pipeline (Python)
        │
        ▼
Processed Layer (processed_workouts)
        │
        ▼
Fact Table (fact_fitness)
        │
        ▼
Analytics + ML Insights
```

---

## ⚙️ Tech Stack

* Python (FastAPI)
* MySQL (Data Storage)
* SQL (Data Processing)
* Docker (Containerization)
* GitHub Actions (CI/CD)
* Machine Learning (Linear Regression)

---

## 🔌 API Endpoints

* `POST /add-workout` → Ingest workout data into raw layer
* `GET /workouts` → Fetch workout records
* `GET /analytics/performance` → User performance insights
* `GET /analytics/calories` → Calorie analysis
* `POST /predict` → Predict calorie burn (ML model)

---

## 🔄 Data Pipeline

1. API ingests workout data into **raw layer**
2. ETL pipeline cleans and transforms data
3. Data is stored in **processed and fact tables**
4. Analytics and ML generate insights

---

## 🚀 ETL Logic

* Calculates calories burned based on workout intensity
* Classifies performance levels
* Aggregates user activity data

---

## 📊 Analytics & Insights

* User performance trends
* Calorie burn analysis
* Workout efficiency tracking

---

## 🤖 Machine Learning (Support Layer)

* Model: Linear Regression
* Predicts calorie burn based on input features
* Used to enhance analytics insights

---

## 🐳 Deployment

* Dockerized application for portability
* CI/CD pipeline using GitHub Actions

---

## 📈 Future Improvements

* Pipeline orchestration (Airflow)
* Real-time streaming (Kafka)
* Dashboard (Streamlit / React)
* Advanced ML models

---

## 🎯 Why This Project Stands Out

* End-to-end **data pipeline implementation**
* Combines backend + ETL + analytics + ML
* Demonstrates real-world system design
* Shows deployment and automation capabilities

---

## 👩‍💻 Author

Sakshi Parve
Aspiring Data Engineer | Backend Developer
