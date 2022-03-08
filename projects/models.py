from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.
class Projects(models.Model):
    title   = models.CharField(max_length=20)
    prelude = models.CharField(max_length=200)
    author = models.CharField(null=True, max_length=30)
    image   = models.ImageField(default="default.png", blank=True, null=True)
    pubdate = models.DateField()
    #THis potentially could be an issue, we could make this a char field
    #projecturlextension = models.CharField(max_length=30
    projurlextension = models.URLField(max_length=40, unique=True)

    def get_absolute_url(self):
        return f"/projects/{self.projurlextension}/"

    def __str__(self):
        return self.title