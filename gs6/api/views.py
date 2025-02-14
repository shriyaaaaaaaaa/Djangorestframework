from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])  # by default if only @api_view() is used, it will be a GET request
# def hello_world(request):
#     return  Response({"message":"Hello, World!"})

@api_view(['GET','POST'])
def hello_world(request):
    
    if request.method == 'GET':
        return Response({"msg": "hi there hiiiiiiiiiiii"})
    if request.method =='POST':
        print(request.data)
        return Response({"mesg":"Hello, world!!!!!!!!!!!","data":request.data})