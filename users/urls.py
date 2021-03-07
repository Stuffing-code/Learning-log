"""Defines URL for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Enable default URL authorization.
    path('', include('django.contrib.auth.urls')),
    # Page registration
    path('register/', views.register, name='register'),
]
