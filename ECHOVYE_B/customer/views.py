from django.shortcuts import render
from .serializers import CustomerSerailaizer
from .models import CustomerDetail
from rest_framework.response import Response
from rest_framework.status import  HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.viewsets import  ModelViewSet
# Create your views here.

class CustomerDetailViewset(ModelViewSet):
    serializer_class = CustomerSerailaizer
    
    def get_queryset(self):
        CustomerModel = CustomerDetail.objects.all()
        return CustomerModel

    def create(self, request, *args, **kwargs):
        customer_query = request.data
        CusName = customer_query['CustomerName']
        CusId = customer_query['CustomerId']
        CusTargetDate = customer_query['CustomerTargetDate']
        CusPhone1 = customer_query['CustomerPhone1']
        CusPhone2 = customer_query['CustomerPhone2']
        CusAddress = customer_query['CustomerAddress']
        CusMail = customer_query['CustomerEmail']
        CusLocationUrl = customer_query['CustomerLocationUrl']

        try:
            CustomerModelUpdate = CustomerDetail.objects.create(CustomerName=CusName,CustomerId=CusId,
                                                                CustomerPhone1=CusPhone1,CustomerPhone2=CusPhone2,
                                                                CustomerTargetDate=CusTargetDate,CustomerAddress=CusAddress,
                                                                CustomerEmail = CusMail,CustomerLocationUrl = CusLocationUrl
                                                                )
            CustomerModelUpdate.save()
            return Response("Succesfully Added!!!",status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response("Failed to Add Customer!!!",status=HTTP_400_BAD_REQUEST)
