from django.contrib import admin

# Register your models here.
from .models import CustomUser, Business

admin.site.register(CustomUser)
admin.site.register(Business)