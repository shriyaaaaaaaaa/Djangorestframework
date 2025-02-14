from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# model  object : single student


def student_detail(request, pk):
    stu=Student.objects.get(id = pk)    # get the student object
    
    serializer=StudentSerializer(stu)   # convert to python obj
    
 #   json_data= JSONRenderer().render(serializer.data)  # convert to json
    
    #We need to send this json data as response to the client: there are many ways one of which is HttpResponse
    
 #   return HttpResponse(json_data, content_type='application/json')  # return json data
 
    return JsonResponse(serializer.data)  # return json data. use this but ensure to import JsonResponse

#this is dict so safe is bydefault true. if it is false then it will not work. so we need to make it true
 
 
#Query-set- All student data   
def student_list(request):
    stu=Student.objects.all()  # get the student object
    
    serializer=StudentSerializer(stu, many=True)   # convert to python obj
    
 #   json_data= JSONRenderer().render(serializer.data)  # convert to json
    
    #We need to send this json data as response to the client: there are many ways one of which is HttpResponse
    
  #  return HttpResponse(json_data, content_type='application/json')  # return json data
      
    return JsonResponse(serializer.data, safe=False)  # return json data. use this but ensure to import JsonResponse

#this is non -dict so safe should be set to false. if it is true then it will not work. so we need to make it false
    
    
   
    
