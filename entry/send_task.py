from utils.producer import send_task
from entry.models import CollectData
from utils.producer import send_task
 
########### parameters need to be sent ##############

# data = CollectData.objects.all()from utils.producer import send_task


# Call send_task() 
def call_send_task(request):
    data = CollectData.objects.all()
    method = {
        'delivery_mode': 2, 
        'content_type': 'application/json'
    }
    body = {"data":data.first().record}
    exchange_name = 'test_exchange'
    queue_name = 'test_queue'
    routing_key = 'test_routing_key'
    return send_task(method, body, exchange_name, queue_name, routing_key)
print(call_send_task())

