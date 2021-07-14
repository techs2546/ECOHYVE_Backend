from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import CustomerDetailViewset

router = DefaultRouter()

router.register('customer-form',CustomerDetailViewset,basename='customer-form')

urlpatterns = [
    url('/',include(router.urls))

]