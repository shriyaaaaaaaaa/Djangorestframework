from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter



#search filter and ordering filters

class studentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[SearchFilter, OrderingFilter]
    search_fields=['name','city']
    ordering_fields=['city']

    
    
    # search_fields=['^name']  #starts-with search    
    
     
    
#http://127.0.0.1:8000/studentapi/?search=kapan    can put either name or city here

    
    
   
   

     
  