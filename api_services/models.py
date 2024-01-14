from django.db import models

# Create your models here.

class Housing(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField()
    description = models.TextField()
    type = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    size = models.CharField(max_length=50)
    beds = models.CharField(max_length=255)
    baths = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.title