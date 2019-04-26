from django.db import models

# Create your models here.
class MovieInfo(models.Model):

    userid = models.CharField(max_length=20, default="",primary_key=True)
    quote = models.CharField(max_length=50, default="")
    comment = models.CharField(max_length=300, default="")

