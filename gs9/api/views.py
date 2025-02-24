from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView

#generic API view and mixin

# class studentList(GenericAPIView, ListModelMixin):
#     queryset= Student.objects.all()
#     serializer_class=StudentSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args, **kwargs)
    
# class studentCreate(GenericAPIView, CreateModelMixin):
#     queryset= Student.objects.all()
#     serializer_class=StudentSerializer
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args, **kwargs)

# class studentretrieve(GenericAPIView,RetrieveModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
# class studentupdate(GenericAPIView,UpdateModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

# class studentdelete(GenericAPIView,DestroyModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)




#list and create : no PK required

class studentLC(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
#retrieve, update and delete : PK required

class studentRUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    