from django.db import models




class Skill(models.Model):
    name = models.CharField(max_length = 50)
    CHOICE_ONE = 'programming_language'
    CHOICE_TWO = 'frameworks'
    CHOICE_THREE = 'libraries'
    CHOICE_FOUR = 'data'
    CHOICE_FIVE = 'database'
    CHOICE_SIX = 'containers'
    CHOICE_SEVEN = 'extra'
    CHOICE_EIGHT = 'social'

    CHOICES = [
        (CHOICE_ONE, 'programming_language'),
        (CHOICE_TWO, 'frameworks'),
        (CHOICE_THREE, 'libraries'),
        (CHOICE_FOUR, 'data'),
        (CHOICE_FIVE, 'database'),
        (CHOICE_SIX, 'containers'),
        (CHOICE_SEVEN, 'extra'),
        (CHOICE_EIGHT, 'social'),
    ]

    type = models.CharField(
        max_length=50,
        choices=CHOICES,
        default=CHOICE_ONE,  # You can set a default value if needed
    )


    def __str__(self):
        return self.name



