from rest_framework import serializers
from admin_app.models import AdminProfile, UserPermission


class AdminProfileSerializer(serializers.Serializer):
    user = serializers.OneToOneField( on_delete=serializers.CASCADE)
    can_manage_users = serializers.BooleanField(default=False)
    can_manage_products = serializers.BooleanField(default=False)
    can_manage_orders = serializers.BooleanField(default=False)
    can_manage_reports = serializers.BooleanField(default=False)

  
    def create(self, data):
        return AdminProfile.objects.create(**data)
    
def update(self, instance, data):
        instance.user = data.get("user", instance.user)
        instance.can_manage_user = data.get("can_manage_user", instance.can_manage_user)
        instance.can_manage_products = data.get("can_manage_products", instance.can_manage_products)
        instance.can_manage_reports= data.get("can_manage_reports", instance.can_manage_reports)
        instance.save()
        
        return instance
    
    
class UserPermissionSerializer(serializers.Serializer):
    user = serializers.ForeignKey( on_delete=serializers.CASCADE)
    can_view_users = serializers.BooleanField(default=False)
    can_create_users = serializers.BooleanField(default=False)
    can_update_users = serializers.BooleanField(default=False)
    can_delete_users = serializers.BooleanField(default=False)

    can_view_products = serializers.BooleanField(default=False)
    can_create_products = serializers.BooleanField(default=False)
    can_update_products = serializers.BooleanField(default=False)
    can_delete_products = serializers.BooleanField(default=False)

    can_view_orders = serializers.BooleanField(default=False)
    can_create_orders = serializers.BooleanField(default=False)
    can_update_orders = serializers.BooleanField(default=False)
    can_delete_orders = serializers.BooleanField(default=False)

    can_view_reports = serializers.BooleanField(default=False)
    can_generate_reports =serializers.BooleanField(default=False)

    def create(self, data):
        return UserPermission.objects.create(**data)



   