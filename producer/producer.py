import time
import json
import random

from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode()
)


price = 180


while True:

    price += random.uniform(-5, 5)

    data = {
        "symbol": "AAPL",
        "price": round(price, 2)
    }

    producer.send("stocks", data)

    print("Produced:", data)

    time.sleep(2)