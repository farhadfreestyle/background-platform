from django.db import models

# Create your models here.


class HomePageData(models.Model):
    welcome = models.TextField()
    about_me = models.TextField()
    my_aim = models.TextField()

