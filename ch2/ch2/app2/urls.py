from django.urls import path
from app2.views import template

urlpatterns = [
    path('temp/', template)
    
]
