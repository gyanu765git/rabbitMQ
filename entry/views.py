from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CollectData
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from utils.producer import send_task
from entry.models import CollectData
from .serializers import CollectDataSerializer
# Create your views here.

class RecordView(APIView):
    @staticmethod
    def post(request):
        method = {
            'delivery_mode': 2, 
            'content_type': 'application/json'
        }
        body = {
            "name":"gyanu",
            "age":23,
            "designation":"software developer"
        }
        exchange_name = 'test_exchange'
        queue_name = 'test_queue'
        routing_key = 'test_routing_key'
        # Call send_task() 
        send_task(method, body, exchange_name, queue_name, routing_key)
        return Response({"success": True, "message": "records created successfully", "data": []},status=HTTP_201_CREATED )
    
    @staticmethod
    def get(request):
        data = CollectData.objects.all()
        serializer_data = CollectDataSerializer(data, many=True).data
        return Response({"success": True, "message": "records are fetched successfully", "data": [serializer_data]}, status=HTTP_200_OK)

