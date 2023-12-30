from django.db import models
from django.utils.text import slugify

# Create your models here.
def experience_image_upload_path(instance, filename):
    return f"experience/{filename}"

class Experience(models.Model):

    CHOICE_ONE = 'tech'
    CHOICE_TWO = 'mentor'
    CHOICE_THREE = 'social'


    CHOICES = [
        (CHOICE_ONE, 'tech'),
        (CHOICE_TWO, 'mentor'),
        (CHOICE_THREE, 'social'),

    ]

    type = models.CharField(
        max_length=50,
        choices=CHOICES,
        default=CHOICE_ONE,  # You can set a default value if needed
    )
    organization_name = models.CharField(max_length = 50)
    job_title = models.CharField(max_length = 50)
    about = models.TextField()
    image = models.ImageField(upload_to=experience_image_upload_path, blank=True)
    slug = models.SlugField(unique=True, blank=True)  # unique slug and can be blank

    def save(self, *args, **kwargs):
        # Generate slug if it's not provided
        if not self.slug:
            self.slug = slugify(self.organization_name)  # Using title to generate slug

        # Call the super method to save the model
        super(Experience, self).save(*args, **kwargs)

    def __str__(self):
        return self.organization_name