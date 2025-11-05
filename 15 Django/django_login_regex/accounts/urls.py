# accounts/urls.py
from django.urls import path
from . import views

# Namespace for the app (used for redirect)
app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
]
