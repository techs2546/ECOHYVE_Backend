from django.db import models

# Create your models here.
class CustomerDetail(models.Model):
    CustomerName = models.CharField(max_length=100)
    Customer_Id = models.CharField(max_length= 30,primary_key = True)
    Address = models.TextField(blank=True,null=True)
    Email = models.EmailField(max_length=55,unique = True)
    Contact_1 = models.CharField(max_length=10)
    Contact_2 = models.CharField(max_length=10,null=True,blank=True)
    Date = models.CharField(max_length=30)
    Location = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Customer_Id



