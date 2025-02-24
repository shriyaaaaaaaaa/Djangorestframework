from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView


#django filter

class studentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filterset_fields=['city','name']
    
     #we have globally defined django filterin settings.py as 
#      REST_FRAMEWORK={
#     'DEFAULT_FILTER_BACKENDS':['django_filters.rest_framework.DjangoFilterBackend']
# }
# 
# now we just set which field is to be filtered.



#http://127.0.0.1:8000/studentapi/?city=kapan  hit this to filter.
    
    
    
   
   
#for locally 

# from django_filters.rest_framework import DjangoFilterBackend
     
     
# class studentList(ListAPIView):
    
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     filter_backends=[DjangoFilterBackend]
#     filterset_fields=['city','name']
    
    
#http://127.0.0.1:8000/studentapi/?city=kapan&name=nitu