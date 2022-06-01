from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import Comment, CustomUser, Film

# Register your models here.

admin.site.register(Film)
admin.site.register(Comment)
admin.site.register(CustomUser)

