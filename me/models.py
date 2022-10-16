from django.db import models
from dashboard.models import GuestLocation


class Message(models.Model):
    message_location = models.ForeignKey(
        GuestLocation, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30, blank=True, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
