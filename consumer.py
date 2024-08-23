import pika
from dotenv import load_dotenv
import os
load_dotenv()
params = pika.URLParameters(os.getenv("RABBITMQ_URL"))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="hello")


print(' [*] Waiting for messages. To exit press CTRL+C')
import json
def callback(ch,method,properties, body):
    print(json.loads(body))
    

channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
print('start consuming')

channel.start_consuming()

channel.close()