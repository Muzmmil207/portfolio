from django import forms
from .models import MyProject, ProjectImage, ProjectTool


class MyProjectForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = ('project_title',
                  'description', 'project_url', 'src_url', 'image', 'tool')

        widgets = {
            'project_title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'image': forms.SelectMultiple(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'project_url': forms.TextInput(attrs={'class': 'form-control'}),
            'src_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
    image = forms.ModelMultipleChoiceField(
        queryset=ProjectImage.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    tool = forms.ModelMultipleChoiceField(
        queryset=ProjectTool.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
