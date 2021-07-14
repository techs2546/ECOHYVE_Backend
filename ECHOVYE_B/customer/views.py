from django.shortcuts import render
from .serializers import CustomerSerailaizer
from .models import CustomerDetail
from rest_framework.viewsets import  ModelViewSet
# Create your views here.

class CustomerDetailViewset(ModelViewSet):
    serializer_class = CustomerSerailaizer
    
    def get_queryset(self):
        query = CustomerDetail.objects.all()
        return query

    def create(self, request, *args, **kwargs):
        pass

