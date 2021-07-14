from .models import CustomerDetail
from rest_framework import serializers
class CustomerSerailaizer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = '__all__'