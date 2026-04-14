# 🏋️ AI-Driven Gym Analytics & Management System

## 🚀 Overview

This project is a backend-driven Gym Management System built using FastAPI and MySQL. It enables real-time member management, attendance tracking, and advanced analytics using ETL pipelines and machine learning. The system is containerized using Docker and integrated with CI/CD for automated builds and validation.

---

## 🧠 Complete Workflow (How the System Works)

### 1️⃣ Data Ingestion (API Layer)

* Users interact with the system through REST APIs.
* APIs like `/members` and `/attendance` collect real-time data.
* FastAPI handles request validation and routing.

---

### 2️⃣ Data Storage (Database Layer)

* All incoming data is stored in MySQL.
* Core tables:

  * `members` → stores user details
  * `attendance` → stores visit records
  * `users` → handles authentication
  * `member_analytics` → stores processed insights

---

### 3️⃣ ETL Pipeline (Data Processing Layer)

* Extracts attendance data from database
* Transforms data into meaningful features:

  * Total visits
  * Visit frequency
  * Churn risk
* Loads processed data into `member_analytics` table
* Uses optimized SQL operations with upsert logic

---

### 4️⃣ Machine Learning (Analytics Layer)

* Logistic Regression model is trained on:

  * Visits
  * Average visits
  * Days since last visit
* Predicts whether a member is:

  * HIGH risk
  * LOW risk

---

### 5️⃣ Business Insights & Optimization

* `/churn` → predicts churn risk for members
* `/insights` → categorizes users (Highly Active, Moderate, Low)
* `/top-members` → uses heap algorithm to find top active members efficiently

---

### 6️⃣ Authentication System

* `/signup` → register new users
* `/login` → authenticate users
* Ensures controlled API access

---

### 7️⃣ Visualization Layer

* Generates attendance charts dynamically using Matplotlib
* Provides visual insights through API endpoints

---

### 8️⃣ Containerization (Docker)

* Application is containerized using Docker
* Ensures:

  * Consistent environment
  * Easy deployment
  * Portability across systems

---

### 9️⃣ CI/CD Pipeline (GitHub Actions)

* Automatically triggers on every code push
* Steps:

  * Install dependencies
  * Validate Python code
  * Build Docker image
* Ensures code quality and automation

---

## ⚙️ Features

* Member Management (CRUD APIs)
* Attendance Tracking System
* Churn Prediction using Machine Learning
* ETL Pipeline for Data Transformation
* Top Active Members using Heap (DSA)
* Authentication (Signup/Login)
* Data Visualization APIs
* Dockerized Deployment
* CI/CD Automation

---

## 🛠️ Tech Stack

* Python, FastAPI
* MySQL
* Pandas, Scikit-learn
* Docker
* Git, GitHub Actions (CI/CD)
* REST APIs, ETL
* Postman (API Testing)
* Data Structures & Algorithms

---

## ▶️ Run Locally

```bash
uvicorn Gym_Management_System:app --reload
```

---

## 🐳 Run with Docker

```bash
docker build -t gym-api .
docker run -p 8000:8000 -e DB_HOST=host.docker.internal gym-api
```

---

## 📊 API Documentation

Access interactive API docs at:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Key Highlights

* End-to-end backend + data engineering + ML system
* Real-world project with deployment and automation
* Demonstrates full development lifecycle (design → build → deploy → automate)

---

## 👩‍💻 Author

Sakshi Parve
