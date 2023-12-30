from django.db import models


# Create your models here.

class Research(models.Model):
    title = models.CharField(max_length = 500)
    description = models.TextField()
    link = models.URLField()
    CHOICE_ONE = 'finished'
    CHOICE_TWO = 'ongoing'



    CHOICES = [
        (CHOICE_ONE, 'finished'),
        (CHOICE_TWO, 'ongoing')

    ]

    type = models.CharField(
        max_length=50,
        choices=CHOICES,
        default=CHOICE_ONE,  # You can set a default value if needed
    )
   

    
    class Meta:
        verbose_name = "Research"
        verbose_name_plural = "Research"



    def __str__(self):
        return self.title