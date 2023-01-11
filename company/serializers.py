from rest_framework import serializers
from .models import Customerdata
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    user=serializers.CharField(max_length=200,required=True)
    phone_number=serializers.IntegerField(required=True)
    email=serializers.CharField(max_length=200,required=True)

    class Meta:
        model = Customerdata
        fields = '__all__'