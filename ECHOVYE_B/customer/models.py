from django.db import models

# Create your models here.
class CustomerDetail(models.Model):
    CustomerName = models.CharField(max_length=100)
    CustomerId = models.CharField(max_length= 30,primary_key = True)
    CustomerAddress = models.TextField(blank=True,null=True)
    CustomerEmail = models.EmailField(max_length=55,unique = True)
    CustomerPhone1 = models.CharField(max_length=10)
    CustomerPhone2 = models.CharField(max_length=10,null=True,blank=True)
    CustomerTargetDate = models.CharField(max_length=30)
    CustomerLocationUrl = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.CustomerId



