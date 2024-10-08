"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls', namespace='app')),
    # path('api/', include('users.urls')),
    path('api/', include('accounts.urls')),
    # path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


]

from rest_framework.routers import DefaultRouter
from dashboard import views as dashboard_views
from billing_app import views as billviews
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register(r'products', dashboard_views.ProductViewSet)
router.register(r'customers', dashboard_views.UserProfileViewSet)
router.register(r'orders', dashboard_views.OrderViewSet)

router.register(r'billing_addresses', billviews.BillingAddressViewSet)
router.register(r'invoices', billviews.InvoiceViewSet)
router.register(r'payments', billviews.PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('dashboard/', dashboard_views.dashboard_view, name='dashboard'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),    
]