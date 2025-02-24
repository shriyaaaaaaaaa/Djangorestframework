from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter




routers=DefaultRouter()

routers.register('studentapi', views.studentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include(routers.urls)),
    
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
    
    
     
     
]

