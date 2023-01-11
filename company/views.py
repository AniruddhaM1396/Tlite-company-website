from tabnanny import check
from unicodedata import name
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from numpy import product
from .models import Customerdata
from rest_framework.views import APIView
from .serializers import CustomerSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

@permission_classes((AllowAny,))
class Customer(APIView):
    #Function to register a User to the App. Uses name as the username.
    def post(self,request):
        user=request.data.get("user")
        print(user)
        phone_number=request.data.get("phone_number")
        print(phone_number)
        #If name or Phone is not provided
        if user is None or phone_number is None:
            return Response({"Error":"Both name and phone_number are required"}, status = status.HTTP_400_BAD_REQUEST)
        
        try:
            if request.data["email"]:
                email = request.data["email"]
                print("email:",email)
        except:
            email="NONE"

        serializer = CustomerSerializer(data=request.data)
        #serialiser.is_valid does the required validation 
        if serializer.is_valid():
            serializer.save()
            subject = 'welcome to GFG world'
            message = f'Hi {user}, thank you for registering in geeksforgeeks.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        