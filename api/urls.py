# urls.py
# URLs in Django resource: https://docs.djangoproject.com/en/4.0/topics/http/urls/
from django.urls import path
from . import views

urlpatterns = [
    path('member/', views.ListMembers.as_view(), name="list_members"),
]