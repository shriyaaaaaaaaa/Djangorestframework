from django.shortcuts import render

def learn_html(req):
    return render(req, 'app2_1/hyper.html' )

def learn_python(req):
    return render(req,'app2_1/python.html')
# Create your views here.
