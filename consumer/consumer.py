import json
from kafka import KafkaConsumer
import psycopg2


# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="stockdb",
    user="admin",
    password="admin"
)

cursor = conn.cursor()


# Kafka consumer
consumer = KafkaConsumer(
    "stocks",
    bootstrap_servers="localhost:9092",

    auto_offset_reset="earliest",

    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)


print("Consumer started...\n")


# Read messages continuously
for message in consumer:

    data = message.value

    symbol = data["symbol"]
    price = data["price"]

    # insert into database
    cursor.execute(
        """
        INSERT INTO stocks(symbol, price)
        VALUES(%s, %s)
        """,
        (symbol, price)
    )

    conn.commit()

    print("Inserted:", data)