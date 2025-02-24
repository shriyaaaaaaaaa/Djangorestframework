from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

#MODEL VIEW SET

# class studentViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer


class studentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer