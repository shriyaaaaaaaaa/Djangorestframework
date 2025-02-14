from django.shortcuts import render

def home(req):
    return render(req, 'core/home.html')



# Create your views here.
