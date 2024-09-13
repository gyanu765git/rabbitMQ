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

def declare_queue(channel, queue_name):
    channel.queue_declare(queue=queue_name, durable=True)

def callback(ch, method, properties, body):
    try:
        logger.info(f"Received message: {body.decode()}")
        # Process the message here

        # Acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"Error processing message: {e}")

def consume(channel, queue_name):
    try:
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
        logger.info(f"Consuming messages from queue: {queue_name}")
    except Exception as e:
        logger.error(f"Error setting up consumer: {e}")

def consume_task(queue_name):
    connection = None
    channel = None
    try:
        connection = get_connection()
        channel = connection.channel()
        declare_queue(channel, queue_name)
        consume(channel, queue_name)
        logger.info('Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except KeyboardInterrupt:
        logger.info('Interrupted')
    except Exception as e:
        logger.error(f"Error during consumption: {e}")
    finally:
        if channel:
            channel.stop_consuming()
            channel.close()
        if connection:
            connection.close()



#########################basic consumer###################
# import pika

# credentials = pika.PlainCredentials('guest', 'guest')
# connection = pika.BlockingConnection(pika.ConnectionParameters(
#     'localhost', 
#     heartbeat=600, 
#     blocked_connection_timeout=300,
#     credentials=credentials
# ))
# channel = connection.channel()

# channel.queue_declare(queue='test_queue', durable=True)

# def callback(ch, method, properties, body):
#     try:
#         print(body)
#         # Process the message here

#         # Acknowledge the message
#         ch.basic_ack(delivery_tag=method.delivery_tag)
#     except Exception as e:
#         print(f"Error processing message: {e}")

# channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=False)

# try:
#     print('Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()
# except KeyboardInterrupt:
#     print('Interrupted')
# finally:
#     channel.stop_consuming()
#     channel.close()
#     connection.close()
