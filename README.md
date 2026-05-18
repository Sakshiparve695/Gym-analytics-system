# 🏋️ GymPulse Analytics Dockerized ETL & Member Insights Platform

## 🚀 Overview

GymPulse is a Dockerized end-to-end gym management analytics platform built using FastAPI, MySQL, Python ETL pipelines, and machine learning–based churn analysis.

The system ingests gym attendance data through REST APIs, processes it using incremental ETL workflows, and generates analytics insights such as member activity tracking, attendance monitoring, and churn risk prediction.

This project demonstrates practical backend engineering and data engineering concepts including:
- REST API development
- Incremental ETL processing
- Dockerized multi-service architecture
- Analytics pipeline design
- Metadata-driven ETL workflows
- Retry and resiliency handling
- Churn prediction using Logistic Regression

---

# 🎯 Problem Statement

Gym management systems often lack automated analytics and operational insights for tracking member engagement and churn behavior.

This project solves that by:

- Building a scalable API-driven attendance system
- Automating ETL-based attendance processing
- Generating analytics-ready member insights
- Predicting churn risk using machine learning
- Implementing production-style Dockerized deployment

---

# 🏗️ System Architecture

```text
Gym Members / Admin
          │
          ▼
FastAPI Backend APIs
          │
          ▼
MySQL Raw Layer
(raw_attendance)
          │
          ▼
Python ETL Pipeline
          │
 ┌──────────────────┐
 ▼                  ▼
Staging Layer       Analytics Layer
(stg_attendance)    (member_analytics)
          │
          ▼
Churn Prediction Engine
(Logistic Regression)
```

---

# ⚙️ Tech Stack

| Category | Technologies |
|---|---|
| Backend | FastAPI, Python |
| Database | MySQL |
| ETL | Python, Incremental Processing |
| Machine Learning | Scikit-learn Logistic Regression |
| DevOps | Docker, Docker Compose |
| Analytics | SQL, Pandas |
| APIs | REST APIs |
| Monitoring | Logging |

---

# ⚡ Key Features

- REST API-based member management
- Attendance tracking system
- Incremental ETL processing using metadata tracking
- Staging and analytics layer architecture
- Churn risk prediction using Logistic Regression
- Dockerized multi-container deployment
- Retry-based MySQL connection handling
- Automated ETL scheduling
- Logging and resiliency support

---

# 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/members` | Add gym member |
| GET | `/members` | View members |
| PUT | `/members/{member_id}` | Update member |
| DELETE | `/members/{member_id}` | Delete member |
| POST | `/attendance` | Mark attendance |
| GET | `/top-members` | View top active members |
| GET | `/churn` | Churn prediction analysis |
| GET | `/insights` | Gym insights and analytics |

---

# 🔄 ETL Pipeline Workflow

## 1️⃣ Extract

New attendance records are extracted incrementally from:

- `raw_attendance`

using metadata tracking from:

- `etl_metadata.last_run`

---

## 2️⃣ Transform

The ETL pipeline:

- validates attendance records
- aggregates member visits
- calculates latest visit dates
- computes activity metrics
- prepares analytics-ready datasets

---

## 3️⃣ Load

Processed data is loaded into:

- `stg_attendance`
- `member_analytics`

---

# 📊 Analytics Features

The analytics layer provides:

- Total member visits
- Last visit tracking
- Attendance monitoring
- Member activity aggregation
- Churn risk analysis
- Top active members insights

---

# 🤖 Churn Prediction Logic

The project uses Logistic Regression to identify members with high churn risk based on:

- total visits
- average visit frequency
- inactivity duration
- recent attendance behavior

Members with low activity or long inactivity periods are marked as higher churn risk.

---

# 🐳 Dockerized Multi-Service Architecture

The project is fully containerized using Docker Compose.

## Services

| Service | Description |
|---|---|
| `api` | FastAPI backend service |
| `db` | MySQL database |
| `etl` | ETL processing service |

---

# ⚙️ Reliability & Resiliency Features

- Retry-based MySQL connection handling
- ETL recovery support using logging
- Dockerized service dependency management
- Incremental ETL execution using metadata tracking
- Automated continuous ETL scheduling
- Environment variable–based credential management

---

# 📂 Database Layers

## Raw Layer
- `raw_attendance`

## Staging Layer
- `stg_attendance`

## Analytics Layer
- `member_analytics`

## Metadata Layer
- `etl_metadata`

---

# 📸 Project Screenshots

## ⚡ FastAPI Swagger Documentation

![FastAPI Docs](screenshots/Docker_FastAPI.png)

---

## 🐳 Dockerized Multi-Service Architecture

![Docker Containers](screenshots/ETL_Docker_Container.png)

---

## 🔄 ETL Pipeline Execution Logs

![ETL Logs](screenshots/GYM_analytics_ETL_Log.png)

---

## 📊 Analytics Layer Output

![Analytics Layer](screenshots/GYM_Analytics_Churn_Risk.png)

---

# 📁 Project Structure

```text
GYM_Management_analytics/
│
├── backend/
├── docker-compose.yml
├── Dockerfile
├── etl.py
├── Gym_Management_System.py
├── requirements.txt
├── screenshots/
├── .env
└── README.md
```

---

# 🚀 Running the Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Sakshiparve695/Gym-analytics-system.git
cd Gym-analytics-system
```

---

## 2️⃣ Configure Environment Variables

Create a `.env` file:

```env
DB_PASSWORD=your_password
```

---

## 3️⃣ Start Docker Containers

```bash
docker-compose up --build
```

---

## 4️⃣ Verify Running Containers

```bash
docker ps
```

---

## 5️⃣ Access FastAPI Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# 📈 Future Improvements

- Power BI / Tableau dashboard integration
- Kafka-based streaming ingestion
- Apache Airflow orchestration
- Cloud deployment on GCP/AWS
- Advanced ML churn prediction models
- Real-time analytics monitoring

---

# 🎯 Why This Project Stands Out

This project demonstrates practical real-world engineering concepts including:

- API-driven data ingestion
- Incremental ETL pipeline design
- Dockerized backend architecture
- Machine learning integration
- Metadata-driven processing
- Production-style debugging and resiliency handling
- Analytics engineering workflows

---

# 👩‍💻 Author

Sakshi Parve
Aspiring Data Engineer & Backend Developer
