from django.contrib import admin
from .models import GuestLocation, MyProject, ProjectImage, ProjectTool
# Register your models here.

admin.site.register(MyProject)
admin.site.register(ProjectImage)
admin.site.register(ProjectTool)
admin.site.register(GuestLocation)
