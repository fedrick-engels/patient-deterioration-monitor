from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_data():
    return {
        "patient_id": random.randint(1, 5),
        "heart_rate": random.randint(60, 140),
        "spo2": random.randint(85, 100),
        "map": random.randint(60, 110),
        "resp_rate": random.randint(12, 30),
        "temp": round(random.uniform(36, 39), 1),
        "timestamp": time.time()
    }

while True:
    data = generate_data()
    producer.send("icu_vitals", data)
    print(data)
    time.sleep(1)