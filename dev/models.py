from django.db import models

# Create your models here.
class Order(models.Model):
    
    user=models.CharField(max_length=200)
    quantity=models.IntegerField()
    total_price=models.IntegerField()
    shipping_address=models.CharField(max_length=200)
    payment_method=models.IntegerField()
    order_status=models