from django.shortcuts import render, redirect
from . import serializers
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
class registerView(APIView):
    serializer_class = serializers.registerSerializers
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid() :
            user =serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/auth/activate/{uid}/{token}"
            email_body = render_to_string('email.html' , {"confirm_link" : confirm_link})
            email_subject = 'Confirm your email'
            email = EmailMultiAlternatives(email_subject  , '' , to = [user.email])
            email.attach_alternative(email_body , 'text/html')
            email.send()
            return Response('check your mail for confirmation')
        return Response(serializer.errors)

def activate(request, uid64, token) :
    try :
        uid = urlsafe_base64_decode(uid64).decode()
        print('uid', uid)
        user = User.objects.get(pk = uid)
    except(User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user , token) :
        user.is_active =True
        user.save()
        return redirect('login')
    else:
        redirect('register')

class loginView(APIView) :
    def post(self, request) :
        serializer = serializers.loginSerializer(data = self.request.data)
        if serializer.is_valid() :
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
    
            user = authenticate(username = username , password = password)
    
            if user :
                token , _ = Token.objects.get_or_create(user = user)
                login(request , user)
                return Response({'token' : token.key , 'user_id' :  user.id})
            return Response({'error' : 'Invalid User'})
        return Response(serializer.errors)
            

    
class logOutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
        