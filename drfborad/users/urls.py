"""drfborad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import RegisterAPIView, RegisterView, ProfileAPIView, ProfileView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('register2/', RegisterView.as_view(), name='register2'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('profile/<pk>/', ProfileAPIView.as_view(), name='profile'),
    path('profile2/<pk>/', ProfileView.as_view(), name='profile2')
]
