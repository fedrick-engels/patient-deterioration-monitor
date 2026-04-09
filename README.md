# Predictive Patient Deterioration Monitor

## Overview
Real-time ICU monitoring system using Kafka, Flink, Spark ML, and Grafana.

## Features
- Real-time streaming
- ML-based risk prediction
- Dashboard visualization

## Run Instructions

1. Start services
docker-compose up

2. Run Kafka producer
python kafka/producer.py

3. Train model
python spark/train_model.py

4. Run API
python api/inference.py

5. Open Grafana
http://localhost:3000
