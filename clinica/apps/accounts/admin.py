from django.contrib import admin
from apps.accounts.models import CustomUser
# Register your models here.
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser)

