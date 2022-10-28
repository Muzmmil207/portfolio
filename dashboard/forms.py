from django import forms

from .models import MyProject, ProjectImage, ProjectTool


class MyProjectForm(forms.ModelForm):
    title = forms.CharField(label='Enter Title', max_length=255, help_text='Required')
    description = forms.Textarea()
    project_url = forms.CharField(label='Project Url', max_length=50, help_text='Required')
    src_url = forms.CharField(label='Source Code Url', max_length=50)
    
    class Meta:
        model = MyProject
        fields = ('title', 'description', 'project_url', 'src_url', 'tool')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Title'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Description'}
        )
        self.fields['project_url'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Enter Url'}
        )
        self.fields['src_url'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Enter Url'}
        )
        self.fields['src_url'].required = False

    def unique_title(self):
        title = self.cleaned_data['title']

        if MyProject.objects.filter(title=title).exists():
            raise forms.ValidationError('Sorry, project with this Title already exists')
        return title
    tool = forms.ModelMultipleChoiceField(
        label='tools',
        queryset=ProjectTool.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class ProjectImageForm(forms.ModelForm):
    
    class Meta:
        model = ProjectImage
        fields = "__all__"

