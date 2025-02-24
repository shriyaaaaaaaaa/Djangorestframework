from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

#concrete view class

class studentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class studentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class studentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class studentupdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class studentdelete(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class studentLC(ListAPIView, CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class studentRD(RetrieveAPIView,  DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class studentRU(RetrieveAPIView, UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class studentRUD(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer