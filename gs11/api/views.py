from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

#viewset


class studentViewSet(viewsets.ViewSet):   
    def list(self,request,pk=None, format=None):
        id =pk                                
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def create(self,request, format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'})
        return Response(serializer.errors)
    
    def update(self,request,pk, format=None):
        id =pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors)
    
    def partial_update(self,request,pk, format=None):
        id =pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk, format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'})
    
    