from django.db import models
from django.utils.text import slugify

# Create your models here.


class Interest(models.Model):
    interest_name = models.CharField(max_length = 50)
    about = models.TextField()
   