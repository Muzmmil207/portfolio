from django import forms
from .models import MyProject


class AboutProjectsForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = ('project_title',  'images',
                  'description', 'project_url', 'src_url')
        widgets = {
            'project_title': forms.TextInput(attrs={'class': 'form-control'}),
            'images': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'multiple': ''}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'project_url': forms.TextInput(attrs={'class': 'form-control'}),
            'src_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
