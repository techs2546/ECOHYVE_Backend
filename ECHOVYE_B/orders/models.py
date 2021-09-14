from django.db import models
from customer.models import CustomerDetail
# Create your models here.
class OrderDetail(models.Model):
    Customer_id = models.ForeignKey(CustomerDetail,on_delete=models.CASCADE)
    OrderId = models.CharField(max_length=70,primary_key = True)
    OrderDate = models.CharField(max_length=30)
    OrderTime = models.CharField(max_length =30)

    def __str__(self):
        return self.OrderId
        