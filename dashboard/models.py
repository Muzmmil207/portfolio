from django.db import models


class GuestLocation(models.Model):
    ip_address = models.CharField(max_length=255)
    city = models.CharField(max_length=75)
    region = models.CharField(max_length=75)
    latitude = models.CharField(max_length=75)
    longitude = models.CharField(max_length=75)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.region


class ProjectTool(models.Model):
    tool = models.CharField(max_length=99)

    def __str__(self):
        return self.tool

class MyProject(models.Model):
    title = models.CharField(
        verbose_name="title",
        help_text="Required",
        max_length=255,
        unique=True
    )
    description = models.TextField(verbose_name="description", help_text="Not Required", blank=True)
    slug = models.SlugField(max_length=125)
    project_url = models.URLField(help_text="Required")
    src_url = models.URLField(blank=True, null=True)
    tool = models.ManyToManyField(
        ProjectTool,
        related_name='tools'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def first_image_url(self):
        try:
            image = self.project_image.first()
            url = image.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    """
    The Project Image table.
    """
    product = models.ForeignKey(MyProject, on_delete=models.CASCADE, related_name="project_image")
    image = models.ImageField(
        verbose_name="image",
        help_text="Upload a product image",
        upload_to="images/",
        default="images/default.png",
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']
