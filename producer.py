import json
import pika
import logging
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_connection():
    try:
        credentials = pika.PlainCredentials('guest', 'guest')
        return pika.BlockingConnection(pika.ConnectionParameters(
            'localhost', 
            heartbeat=600, 
            blocked_connection_timeout=300,
            credentials=credentials
        ))
    except Exception as e:
        logger.error(f"Error connecting to RabbitMQ: {e}")
        raise

def declare_exchange_and_queue(channel, exchange_name, queue_name, routing_key):
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)
    channel.queue_declare(queue=queue_name, durable=True)
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

def publish(channel, method, body, exchange='', routing_key=''):
    try:
        properties = pika.BasicProperties() if not isinstance(method, dict) else pika.BasicProperties(**method)
        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=json.dumps(body), properties=properties)
        logger.info(f"Message published successfully. Exchange: {exchange}, Routing Key: {routing_key}")
    except Exception as e:
        logger.error(f"Error publishing message: {e}")

def send_task(method, body, exchange_name, queue_name, routing_key):
    connection = None
    channel = None
    try:
        connection = get_connection()
        channel = connection.channel()
        declare_exchange_and_queue(channel, exchange_name, queue_name, routing_key)
        logger.info("Publishing message: %s", body)
        publish(channel, method, body, exchange=exchange_name, routing_key=routing_key)
    except Exception as e:
        logger.error(f"Error sending task: {e}")
    finally:
        if channel:
            channel.close()
        if connection:
            connection.close()



################################################# simple setup for producer ###############################

# import pika

# credentials = pika.PlainCredentials('guest', 'guest')
# connection = pika.BlockingConnection(pika.ConnectionParameters(
#     'localhost', 
#     heartbeat=600, 
#     blocked_connection_timeout=300,
#     credentials=credentials
#     ))
# channel = connection.channel()

# def declare_exchange_and_queue(channel, exchange_name, queue_name, routing_key):
#     channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)
#     channel.queue_declare(queue=queue_name, durable=True)
#     channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

# def send_test_task(exchange_name, routing_key, body):
#     declare_exchange_and_queue(channel, exchange_name, queue_name, routing_key)
#     channel.basic_publish(exchange = exchange_name, routing_key = routing_key, body = body)



############# rabbit mq connecttion by AMQP url #############################################

# params = pika.URLParameters('amqps://sbyndfnvvu:XUKLGkwXzAh7MYAvkq1fsfsfYBxHEF-pbdfaf1neb@shadfark.rmq.cloudamqp.com/sbasynnadfvvu')
# connection = pika.BlockingConnection(params)
# channel = connection.channel()

# def publish(method, body):
#     properties = pika.BasicProperties(method)
#     channel.basic_publish(exchange='', routing_key='user_registration', body=json.dumps(body), properties=properties)

