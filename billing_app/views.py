from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class BillingAddressViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BillingAddressSerializer

    def get_queryset(self):
        """
            should return address of the authenticated user or customer
        """
        return BillingAddress.objects.filter(customer__user=self.request.user)

class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        """
            should return specific customer's invoice
        """
        return Invoice.objects.filter(customer__user=self.request.user)

class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        """
            should return specific customer's payment
        """
        return Payment.objects.filter(invoice__customer__user=self.request.user)
