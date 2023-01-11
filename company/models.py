from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customerdata(models.Model):
    user=models.CharField(max_length=50)
    phone_number=models.IntegerField(null=False, unique=True)
    email=models.EmailField(max_length=50, null=True)

    def __str__(self):
        return str(self.user)
