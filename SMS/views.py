from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework import status
from django.conf import settings
from . models import LoginData,BatchData,StudentData,DateData,SendOTP
from . serializer import LoginDataSerializer,BatchDataSerializer,StudentDataSerializer,DateDataSerializer,SendOTPSerializer

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def Login_Data(request):
    if request.method == 'GET':
        Item_Data = LoginData.objects.all()
        serializer = LoginDataSerializer(Item_Data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        Data = LoginDataSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status= HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        try:
            item = LoginData.objects.get(pk=request.data.get('id'))
        except LoginData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LoginDataSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            item = LoginData.objects.get(pk=request.data.get('id'))
        except LoginData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Batch_Data(request):
    if request.method == 'GET':
        items = BatchData.objects.all()
        serializer = BatchDataSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BatchDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            item = BatchData.objects.get(pk=request.data.get('id'))
        except BatchData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BatchDataSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            item = BatchData.objects.get(pk=request.data.get('id'))
        except BatchData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST','PUT','DELETE'])
def Student_Data(request):
    if request.method == 'GET':
        Item_Data = StudentData.objects.all()
        serializer = StudentDataSerializer(Item_Data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        Data = StudentDataSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

    elif request.method == 'PUT':
        try:
            item = StudentData.objects.get(pk=request.data.get('id'))
        except StudentData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentDataSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            item = StudentData.objects.get(pk=request.data.get('id'))
        except StudentData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST','PUT','DELETE'])
def Date_Data(request):
    if request.method == 'GET':
        Item_Data = DateData.objects.all()
        serializer = DateDataSerializer(Item_Data, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        Data = DateDataSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

    elif request.method == 'PUT':
        try:
            item = DateData.objects.get(pk=request.data.get('id'))
        except DateData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DateDataSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            item = DateData.objects.get(pk=request.data.get('id'))
        except DateData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
api_view(['GET','POST'])
def Send_OTP(request):
    if request.method == 'GET':
        Item_Data = SendOTP.objects.all()
        serializer = SendOTPSerializer(Item_Data, many=True)
        return Response(serializer.data)
    
    
def contains_alphanumeric(s):
    return any(char.isalnum() for char in s)

@api_view(['GET', 'POST'])
def Send_OTP(request):
    if request.method == 'GET':
        Item_Data = SendOTP.objects.all()
        serializer = SendOTPSerializer(Item_Data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('Email')
            otp = serializer.validated_data.get('OTP').split(' ')[0]
            mailtype = serializer.validated_data.get('OTP').split(' ')[1]
            print(mailtype)
            if mailtype == 'Username':
                title = 'Forgot Username'
                message = f'''Dear User,
                
Your username is {otp}.
Please keep this information secure and do not share it with anyone. If you did not request this information, please disregard this message and ensure your account security is intact.
If you have any concerns or questions, feel free to contact our support team.

Thank you,
VCUBE Support Team.
'''
            else:
                title = 'Forgot Password'
                message = f'''Dear User,
                
Please use the following OTP code, {otp}, to reset your password.
Ensure to input the code accurately to proceed with the password reset process. If you did not initiate this request, please disregard and ensure your account security is intact.
If you have any concerns or questions, feel free to contact our support team.

Thank you,
VCUBE Support Team.
'''
            send_mail(
                title,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    