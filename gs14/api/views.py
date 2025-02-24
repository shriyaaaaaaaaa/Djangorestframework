from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

#MODEL VIEW SET session authentication

class studentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticated]    #AllowAny and IsAdminUser works the same as BasicAuthentication
    
# IsAuthenticated "detail": "Authentication credentials were not provided." is shown and no prompt is given to include our credentials

    # permission_classes=[IsAuthenticatedOrReadOnly]     #allows only authorized user to write (logged in), and unauthorized can only read the data.
    
     
    #permission_classes=[DjangoModelPermissions]   #should give users model permission in order to update, change or delete data.
    #igonores unauthenticated user, authenticated user with no model permissions can read the data
    
    #put, patch -> add change permission, delete -> delete permission, post-> add permission
    
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]   #same as DjangoModelPermissions but allow unauthenticated user to read.
    
    