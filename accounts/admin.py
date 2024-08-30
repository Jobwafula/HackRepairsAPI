from django.contrib import admin

# Register your models here.
from .models import CustomUser, Business

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')

admin.site.register(CustomUser,AuthorAdmin)

admin.site.register(Business)