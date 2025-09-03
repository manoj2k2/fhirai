import pika
from fhir_agent import config

def normalize(data: str) -> str:
    """Normalizes the input data."""
    # Add normalization logic here
    return data.strip()

def tokenize(data: str) -> list[str]:
    """Tokenizes the input data."""
    # Add tokenization logic here
    return data.split()

def send_to_rabbitmq(data: str):
    """Sends data to RabbitMQ."""
    connection = pika.BlockingConnection(pika.ConnectionParameters(config.RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=config.RABBITMQ_QUEUE)
    channel.basic_publish(exchange="", routing_key=config.RABBITMQ_QUEUE, body=data)
    connection.close()
