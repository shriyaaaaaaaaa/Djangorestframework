from rest_framework import serializers
from .models import Student


#model serializer
        
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Student
#         fields=['id','name','roll','city']
        


#model serializer with read_only_fields

class StudentSerilaizer(serializers.ModelSerializer):

    #name = serializers.CharField(read_only=True)  #this field won't be updated.
    class Meta:
        model=Student
        fields=['id','name','roll','city']
        read_only_fields=['name','city']      #these fields eon't be updated.
#  extra_kwargs={'name':{'read_only':True}}  #this field won't be updated.


#modelserializer with validators

class StudentSerializer(serializers.ModelSerializer):
    #validators: validation logic into reusable code
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name Should be start with R')
        
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    class Meta:
        model=Student
        fields=['id','name','roll','city']
        
    #field level validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #object level validation
    
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='ravi' and ct.lower()!='delhi':
            raise serializers.ValidationError('City Must be Delhi')
        
        