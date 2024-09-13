from producer import send_task
 
########### parameters need to be sent ##############
method = {
    'delivery_mode': 2, 
    'content_type': 'application/json'
}
body = {
    'user_id': '3kadaddfeydfjadjljajlajfalfjalkjj',
    'name': 'dummy human'
}
exchange_name = 'test_exchange'
queue_name = 'test_queue'
routing_key = 'test_routing_key'

# Call send_task() 
send_task(method, body, exchange_name, queue_name, routing_key)
