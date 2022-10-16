from django.contrib import admin
from .models import GuestLocation, MyProject
# Register your models here.

admin.site.register(MyProject)
admin.site.register(GuestLocation)
