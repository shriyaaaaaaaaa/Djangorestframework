from django.shortcuts import render
from .serializers import SongSerializer, SingerSerializer
from .models import Song, Singer
from rest_framework import viewsets


#serializer relations in drf

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


