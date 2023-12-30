from django.db import models


# Create your models here.

class Research(models.Model):
    title = models.CharField(max_length = 500)
    description = models.TextField()
    link = models.URLField()
   

    
    class Meta:
        verbose_name = "Research"
        verbose_name_plural = "Research"



    def __str__(self):
        return self.title