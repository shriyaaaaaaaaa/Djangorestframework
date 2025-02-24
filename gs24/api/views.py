from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from .mypaginations import Mypagination

# Create your views here.
#page number pagination

class studentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=Mypagination
    
    
    
#to define globally go in settings.py and add this line in rest_framework
# 'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
# 'PAGE_SIZE':2,    #page size of your choice
#http://127.0.0.1:8000/student/?page=2    can write page=3 to got to 3 if page size is more than 2