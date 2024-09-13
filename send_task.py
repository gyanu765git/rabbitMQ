from producer import send_task
import json

body = {
    "message": "I am gyanu chauhan , software developer, i like mango"
}

send_task("message sent successfully", body = body, queue_name= 'test_queue', exchange_name="test_exchange", routing_key="test_routing_key")
