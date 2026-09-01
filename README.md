# E-commerce Sales ETL Pipeline

## 📌 Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Python, Pandas, and PostgreSQL.

The pipeline extracts e-commerce sales data from a CSV file, validates and transforms the data, and loads the processed data into PostgreSQL for analysis.

## 🏗️ Architecture

CSV File
   ↓
Extract
   ↓
Pandas DataFrame
   ↓
Data Validation
   ↓
Transform
   ↓
PostgreSQL
   ↓
SQL Analysis

## 🛠️ Technologies Used

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Psycopg2
- Git
- GitHub

## 📂 Project Structure

```text
ecommerce-etl/
│
├── data/
│   └── sales.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── db_connection.py
│   ├── logger_config.py
│   └── main.py
│
├── logs/
│
├── .gitignore
├── requirements.txt
└── README.md