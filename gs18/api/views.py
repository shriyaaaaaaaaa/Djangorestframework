from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.customauth import CustomAuthentication

#Custom authentication

class studentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]   
    
    