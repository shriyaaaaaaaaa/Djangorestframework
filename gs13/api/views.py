from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

#MODEL VIEW SET basic authentication

class studentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    #permission_classes=[AllowAny]   anyone can access
    # permission_classes=[IsAdminUser]    #special user can access, staff status ticked ones.
    
    # suppose we have many classes and all needs authentication in that case 
    # we can globally aunthenticate by going to settings.py 


#here because we have set authenticated all types of user can login and see the data by putting the credentials

#normaluser, superuser, admin. 
# normaluser can only see the data,   : In permission only checked on active
# superuser can add and see the data,   : ticked on active, staff, superuser status 
# admin can add, delete, update and see the data. : ticked on active, staff status