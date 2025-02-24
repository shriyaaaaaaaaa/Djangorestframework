from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView




routers=DefaultRouter()

routers.register('studentapi', views.studentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include(routers.urls)),
    
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),  
     
     
]

#acccess token is valid for 5 minutes after which you can't acccess api through that token.
#we can use refresh token to generate another access token.

#http POST http://127.0.0.1:8000/gettoken/ username="" password=""
#http POST http://127.0.0.1:8000/verifytoken/ token="give accesstoken"
#http POST http://127.0.0.1:8000/refreshtoken/ refresh="give refreshtoken"


#https://jwt.io/
