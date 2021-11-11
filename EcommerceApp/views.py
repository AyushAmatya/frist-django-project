from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from EcommerceApp.serializers import CustomerSerializers, ItemsSerializers
from EcommerceApp.models import Customers,Items

# Create your views here.

@csrf_exempt
def customerApi (request, id=0):
    if request.method == 'GET':
        customers = Customers.objects.all()
        customer_serializer = CustomerSerializers(customers,many=True)
        return JsonResponse(customer_serializer.data,safe=False)
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializers(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Customer Added Sucessfully", safe=False)
        return JsonResponse("Failed to add Customer", safe=False)
    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer = Customers.objects.get(CustomerId = customer_data['CustomerId'])
        customer_serializer = CustomerSerializers(customer,data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Updated Customer Sucessfully", safe=False)
        return JsonResponse("Failed to update Customer", safe=False)
    elif request.method == 'DELETE':
        customer = Customers.objects.get(CustomerId = id)
        customer.delete()
        return JsonResponse("Deleted Customer Sucessfully", safe=False)
