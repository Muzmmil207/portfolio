from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
default_img = 'https://images.unsplash.com/photo-1515879218367-8466d910aaa4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80'


class GuestLocation(models.Model):
    ip_address = models.CharField(max_length=255)
    city = models.CharField(max_length=75)
    region = models.CharField(max_length=75)
    latitude = models.CharField(max_length=75)
    longitude = models.CharField(max_length=75)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.region


class MyProject(models.Model):
    project_title = models.CharField(max_length=99)
    description = models.TextField(blank=True, null=True)
    project_url = models.URLField()
    src_url = models.URLField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    image = models.ManyToManyField(
        'ProjectImage',
        related_name='images'
    )
    tool = models.ManyToManyField(
        'ProjectTool',
        related_name='tools'
    )

    @property
    def get_clean_url(self):
        url = self.project_title
        return '-'.join(i for i in url.split())

    @property
    def image_url(self):
        try:
            image = self.image.first()
            url = image.image.url
        except:
            url = default_img
        return url

    def __str__(self):
        return f'{self.project_title}'


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='img/')
    order = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f' {self.image}'


class ProjectTool(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return f'{self.name}'
