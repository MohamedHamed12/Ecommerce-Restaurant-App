from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, Profile



class CustomUserAdmin(admin.ModelAdmin):
    fields = ['id', 'email','first_name', 'last_name', 'email_confirmed', 'profile_completed']
    list_display = ['id','email', 'first_name', 'last_name', 'email_confirmed', 'profile_completed']
admin.site.register(CustomUser, CustomUserAdmin)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'bio', 'profile_image', 'date_of_birth', 'phone_number']

    list_display = ['user', 'bio', 'profile_image', 'date_of_birth', 'phone_number']

admin.site.register(Profile, ProfileAdmin)

