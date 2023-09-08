from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .models import FrontendUsers
from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your views here.

class signupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    contact = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = FrontendUsers
        fields = ["email", "username", "contact","password"]

    def validate(self, data):
        check = FrontendUsers.objects.filter(email= data['email']).first()

        if check is not None:
            raise serializers.ValidationError('Email already exist')
        
        return(data)
    
    def create(self, data):
        pwd = data['password']
        new_pwd = make_password(pwd)
        data['password'] = new_pwd

        new_user = FrontendUsers.objects.create(**data)

        return new_user
    
@api_view(['POST'])
def Signup(request):
    try:
        serializedata = signupSerializer(data= request.data)

        if serializedata.is_valid():
            serializedata.save()
            return Response(data={"message":'Signup successful', "info": request.data})
        else:
            return Response(serializedata.errors)

    except BaseException as e:
        return Response(str(e))
        
    
class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def logUser(self, data):
        user = FrontendUsers.objects.filter(email = data['email']).first()

        

        if user is None:
            return 'Invalid email'
        else:
            encpwd = getattr(user, 'password')
            op = data['password']
            

            check = check_password(op, encpwd)
            if check:
                data = {
                    "id": getattr(user, 'id'),
                    "email": getattr(user, 'email'),
                    "username": getattr(user, 'username'),
                    "contact": getattr(user, 'contact')
                }
                return data
            else:
                return 'Invalid Password'
            
@api_view(['POST'])
def Login(request):
    try:
        if request.data['email'] == "":
            return Response(data="Email field is empty")
        elif request.data['password'] == "":
            return Response(data="Password field is empty")
        elif request.data['email'] == "" and request.data['password'] == "":
            return Response(data="Both email and password fields are empty")
        else: 
            serializedata = loginSerializer(data = request.data)
            if serializedata.is_valid():
                 result = serializedata.logUser(serializedata.data)
                 print(result)
                 return Response(result)
                
            else:
                return Response(serializedata.errors)        
    except BaseException as e:
        return Response(str(e))


class updateSerializer(serializers.ModelSerializer):
    otherName = serializers.CharField()
    # dateOfBirth = serializers.DateField()
    gender = serializers.CharField()

    class Meta:
        model = FrontendUsers
        fields = '__all__' 

@api_view(['PATCH'])
def UpdateAccount(request, email):
    try:
        user = FrontendUsers.objects.filter(email = email).first()

        if user is None:
            return Response('No account found')
        else:
            serializedata = updateSerializer(instance= user, data= request.data, partial=True)
            if serializedata.is_valid():
                serializedata.save()
                return Response(data= serializedata.data)
            else:
                return Response(serializedata.errors)
    except BaseException as e:
        return Response(str(e))

@api_view(['DELETE'])
def DeleteAccount(request, email):
    try:
        user = FrontendUsers.objects.filter(email = email).first()

        if user is None:
            return Response('Account not found')
        else:
            user.delete()
            return Response('Account deleted successfully')
        
    except BaseException as e :
        return Response(str(e))