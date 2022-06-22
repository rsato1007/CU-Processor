# urls.py
# URLs in Django resource: https://docs.djangoproject.com/en/4.0/topics/http/urls/
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.Users.as_view(), name='User'),
    path('member/', views.Members.as_view(), name="member"),
]