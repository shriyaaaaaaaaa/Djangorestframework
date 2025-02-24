from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView


#filtering

class studentList(ListAPIView):
    queryset=Student.objects.filter(passby='user1')
    serializer_class=StudentSerializer
    
    
    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(passby=user)    #the user(w staff status) that logins only sees their passed student in the list
    
    
    
    #queryset=Student.objects.filter(passby='user1')   : only shows passby user1 while listing all
