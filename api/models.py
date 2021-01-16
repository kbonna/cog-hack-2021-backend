from django.db import models

# Create your models here.
class Face(models.Model):
    image = models.ImageField(upload_to="api_images")

    def __str__(self):
        return f"Face(pk={self.pk})"