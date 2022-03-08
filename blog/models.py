from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.
class Blogg(models.Model):
    title   = models.CharField(max_length=20)
    prelude = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(null=True, max_length=30)
    image   = models.ImageField(default="default.png", blank=True, null=True)
    pubdate = models.DateField()

    def get_absolute_url(self):
        # return reverse("blog:blog-view", kwargs={"id":self.id})
        return f"/blog/{self.id}/"

    def __str__(self):
        return self.title
