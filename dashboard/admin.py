from django.contrib import admin
from product_app.models import Product
from user_app.models import UserProfile, Order

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(Product)

