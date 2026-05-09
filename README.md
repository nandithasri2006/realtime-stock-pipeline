# Real-Time Stock Market Data Pipeline

A real-time data engineering project that streams live stock price data using Python, processes events through :contentReference[oaicite:1]{index=1}, stores data in :contentReference[oaicite:2]{index=2}, and visualizes metrics using :contentReference[oaicite:3]{index=3}.

---

## Project Overview

This project simulates a production-grade streaming system:

Stock Data Producer → Kafka → Consumer → PostgreSQL → Grafana Dashboard

Features:

- Real-time stock data generation
- Event streaming using Kafka
- Database storage
- Live dashboard visualization
- Containerized deployment using :contentReference[oaicite:4]{index=4}

---

## Architecture

```text
Python Producer
      ↓
Apache Kafka
      ↓
Python Consumer
      ↓
PostgreSQL
      ↓
Grafana Dashboard
```

---

## Tech Stack

- Python
- :contentReference[oaicite:5]{index=5}
- :contentReference[oaicite:6]{index=6}
- :contentReference[oaicite:7]{index=7}
- :contentReference[oaicite:8]{index=8}
- :contentReference[oaicite:9]{index=9}
- JSON

---

## Folder Structure

```text
realtime-stock-pipeline/
│
├── producer/
│   └── producer.py
│
├── consumer/
│   └── consumer.py
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup Instructions

### 1. Clone repository

```bash
git clone <your-repo-url>
cd realtime-stock-pipeline
```

---

### 2. Create virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Start containers

```bash
docker compose up -d
```

---

### 5. Create database table

```bash
docker exec -it postgres psql -U admin -d stockdb
```

SQL:

```sql
CREATE TABLE stocks(
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20),
    price FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 6. Run producer

```bash
cd producer
python producer.py
```

---

### 7. Run consumer

```bash
cd consumer
python consumer.py
```

---

### 8. Open dashboard

Grafana:

```text
http://localhost:3000
```

Default login:

```text
admin / admin
```

---

## Sample Output

Producer:

```text
Produced: {'symbol': 'AAPL', 'price': 182.45}
```

Consumer:

```text
Inserted: {'symbol': 'AAPL', 'price': 182.45}
```

---

## Dashboard

Real-time visualization of stock prices for:

- :contentReference[oaicite:10]{index=10}
- :contentReference[oaicite:11]{index=11}
- :contentReference[oaicite:12]{index=12}
- :contentReference[oaicite:13]{index=13}

---

## Future Improvements

- Multiple stock symbols
- Alerting system
- REST API integration
- Machine learning forecasting
- Cloud deployment

---

## Author

Nandhitha Sri
