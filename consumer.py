import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', 
    heartbeat=600, 
    blocked_connection_timeout=300,
    credentials=credentials
    ))
channel = connection.channel()

channel.queue_declare(queue='test_queue', durable=True)

def callback(ch, method, properties, body):
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='test_queue',on_message_callback=callback)

channel.start_consuming()

channel.close()



    