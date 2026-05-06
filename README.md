# 🏋️ 🏋️ GymPulse Analytics
Dockerized ETL & Member Insights Platform

## 🚀 Overview

This project is a Dockerized end-to-end Gym Management Analytics platform built using FastAPI, MySQL, and Python ETL pipelines.

The system ingests gym attendance data, processes it through an incremental ETL pipeline, and generates analytics insights such as member visit tracking and churn risk analysis.

The project demonstrates practical data engineering concepts including:
- ETL pipeline design
- Incremental data processing
- Staging architecture
- Docker container orchestration
- Health checks and resilient startup handling
- Analytics table generation

---

# 🏗️ Architecture

```text
FastAPI API
     ↓
raw_attendance
     ↓
ETL Pipeline (Python)
     ↓
stg_attendance
     ↓
member_analytics
     ↓
Churn Analytics
```

---

# ⚙️ Tech Stack

## Backend
- FastAPI
- Python

## Database
- MySQL

## Data Engineering
- ETL Pipeline
- Incremental Loading
- Staging Tables
- Metadata Tracking

## DevOps / Deployment
- Docker
- Docker Compose

## Analytics
- Churn Risk Analysis
- Visit Tracking

---

# 🔌 API Features

- Add gym attendance records
- Fetch attendance data
- Process attendance through ETL pipeline
- Generate analytics insights

---

# 🔄 ETL Pipeline Workflow

## 1. Extract
New attendance records are extracted from:
- `raw_attendance`

using incremental loading based on:
- `etl_metadata.last_run`

---

## 2. Transform
The ETL pipeline:
- validates records
- aggregates member visits
- calculates latest visit date
- computes churn risk indicators

---

## 3. Load
Processed data is loaded into:
- `member_analytics`

---

# 📊 Analytics Features

The analytics layer provides:

- Total member visits
- Last visit tracking
- Churn risk analysis
- Member activity aggregation

---

# ⚡ Churn Risk Logic

Members are currently marked as churn risk when:

```sql
total_visits < 5
```

This can later be extended with:
- inactivity duration
- attendance frequency
- machine learning models

---

# 🐳 Dockerized Architecture

The project is fully containerized using Docker Compose.

## Services

- `api` → FastAPI backend
- `db` → MySQL database
- `etl` → ETL processing service

---

# 🔧 Production-Style Features Implemented

## ✅ Retry-Based DB Connection Handling
ETL service retries database connections until MySQL becomes available.

## ✅ Docker Health Checks
MySQL health checks ensure dependent services start only after DB readiness.

## ✅ Incremental ETL Processing
Only newly inserted records are processed during each ETL cycle.

## ✅ Continuous ETL Scheduler
ETL runs automatically at scheduled intervals.

## ✅ Environment Variable Management
Sensitive credentials managed using `.env`.

---

# 📂 Database Tables

## Raw Layer
- `raw_attendance`

## Staging Layer
- `stg_attendance`

## Analytics Layer
- `member_analytics`

## Metadata Layer
- `etl_metadata`

---

# 🚀 Running the Project

## Clone Repository

```bash
git clone <your-repo-link>
```

---

## Start Containers

```bash
docker-compose up --build
```

---

## Verify Running Containers

```bash
docker ps
```

---

# 📸 Project Screenshots

Screenshots included for:
- Docker containers
- ETL logs
- Analytics outputs
- Churn analysis

---

# 📈 Future Improvements

- Power BI / Tableau dashboard
- Kafka streaming integration
- Airflow orchestration
- Advanced churn prediction models
- Cloud deployment

---

# 🎯 Why This Project Stands Out

This project demonstrates practical real-world data engineering concepts including:

- API-driven data ingestion
- ETL pipeline architecture
- Incremental processing
- Container orchestration
- Analytics engineering
- Production-style debugging and resiliency

---

# 👩‍💻 Author

**Sakshi Parve**

Aspiring Data Engineer
