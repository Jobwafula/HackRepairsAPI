from django.urls import path
from .views import register_user, user_login, user_logout, change_password, create_business, get_business, update_business, get_business_all, delete_business
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),


    path('password_reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            html_email_template_name='registration/password_reset_email.html'
            ), 
            name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),


    path('add_businesses/', create_business, name='create_business'),
    path('businesses/', get_business_all, name='get_business_all'),
    path('businesses/<int:pk>/', get_business, name='get_business'),
    path('businesses/<int:pk>/update/', update_business, name='update_business'),
    path('businesses/<int:pk>/delete/', delete_business, name='delete_business' ),
] 

