import pika
from django.conf import settings
from dotenv import load_dotenv
import os
load_dotenv()
RABBITMQ_URL = os.getenv("RABBITMQ_URL")
params = pika.URLParameters(RABBITMQ_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="django_server")


def publish(data):
    global channel,connection
    if channel.is_closed or connection.is_closed:
        connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_URL))
        channel = connection.channel()
    import json
    channel.basic_publish(exchange="", routing_key="django_server", body=json.dumps(data))
    
    print(data)
    