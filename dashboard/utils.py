from django.conf import settings
from .models import GuestLocation
import requests


def get_location():

    def get_ip():
        response = requests.get('https://api64.ipify.org?format=json').json()
        ip = response["ip"]
        return ip

    ip = get_ip()
    location_data = requests.get(
        f'http://ipinfo.io/{ip}?token={settings.API_TOKEN}').json()

    GuestLocation.objects.get_or_create(
        ip_address=location_data['ip'],
        city=location_data['city'],
        region=location_data['region'],
        latitude=location_data['loc'].split(',')[0],
        longitude=location_data['loc'].split(',')[1],
    )

    return location_data['ip']
