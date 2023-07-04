from dataclasses import field
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer

# from .views import send_confirmation_email
from .models import CustomUser, Profile
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework import serializers

class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD

def send_confirmation_email(user,request):
    print('send_confirmation_email')
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    mail_subject = 'Activate your account'
    message = render_to_string('/run/media/mohamed/New Volume/Documents/programing/django/restaurant/Ecommerce-Restaurant-App/backend/accounts/templates/activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': uid,
        'token': token
    })
    email = EmailMessage(mail_subject, message, to=[user.email])
    email.content_subtype = 'html'  
    email.send()
    print('done_email')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        # model = get_user_model()
        model = CustomUser
        fields = ('first_name', 'last_name','email','password')

class ProfileSerializer(serializers.ModelSerializer):
   # user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'
