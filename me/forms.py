from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name',  'email', 'subject', 'message')

    def get_info(self):
        # get clean data from the request object
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):
        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
