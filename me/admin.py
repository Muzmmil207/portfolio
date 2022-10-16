from django.contrib import admin
from .models import Message
from django.contrib.sessions.models import Session
# Register your models here.

admin.site.register(Message)
