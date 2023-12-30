from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    linkedln_url = models.URLField()
    linkedln_username = models.CharField(max_length=50)
    facebook_url = models.URLField()
    facebook_username = models.CharField(max_length=50)
    instagram_url = models.URLField()
    instagram_username = models.CharField(max_length=50)
    twitter_url = models.URLField()
    twitter_username = models.CharField(max_length=50)
    github_url = models.URLField()
    github_username = models.CharField(max_length=50)
    medium_url = models.URLField()
    medium_username = models.CharField(max_length=50)


