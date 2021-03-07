"""Defines URL for users"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Enable default URL authorization.
    path('', include('django.contrib.auth.urls')),
]