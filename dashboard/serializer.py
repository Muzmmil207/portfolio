from .models import GuestLocation
from rest_framework import serializers


class GuestLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestLocation
        fields = '__all__'
