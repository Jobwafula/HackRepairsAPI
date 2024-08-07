from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from product_app.models import Product
from user_app.models import UserProfile, Order
from .serializers import *

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
     A simple viewset for retrieving all products available
    """
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    """
     A simple viewset for retrieving all available authenticated users
    """
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
     A simple viewset for retrieving all orders made
    """
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer