from flask import Flask, jsonify
from confluent_kafka import Producer

app = Flask(__name__)

# Kafka configuration
kafka_config = {
    'bootstrap.servers': 'kafka:9092',  # Adjust the Kafka broker address
}

# Kafka topic
kafka_topic = 'my-topic'

# Kafka producer instance
producer = Producer(kafka_config)


def delivery_report(err, msg):
    """Callback function to be executed on successful message delivery or in case of an error."""
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')


@app.route('/produce')
def produce_message():
    """Flask route that produces a Kafka message."""
    message = 'Hello, Kafka!'

    # Produce the message to the Kafka topic
    producer.produce(kafka_topic, key='key', value=message, callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery reports received.
    producer.flush()

    return jsonify({'message': message, 'status': 'Message sent to Kafka'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5008)
