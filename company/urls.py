from django.urls import path
from company.views import Customer


urlpatterns=[
    
    path('customer/',Customer.as_view(),name='customer'),
    
]