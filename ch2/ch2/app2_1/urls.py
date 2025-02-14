from django.urls import path
from app2_1.views import learn_html,learn_python

urlpatterns = [
    path('', learn_html ),
    path('py/', learn_python),
    
]
