from django.db import models
from django.utils.text import slugify

# Create your models here.
def education_image_upload_path(instance, filename):
    return f"education/{filename}"

class Education(models.Model):
    school_name = models.CharField(max_length = 50)
    major = models.CharField(max_length = 50)
    startdate = models.DateField(null=True, default=None)
    enddate = models.DateField(null=True, default=None)
    about = models.TextField()
    image = models.ImageField(upload_to=education_image_upload_path, blank=True)
    slug = models.SlugField(unique=True, blank=True)  # unique slug and can be blank

    def save(self, *args, **kwargs):
        # Generate slug if it's not provided
        if not self.slug:
            self.slug = slugify(self.school_name)  # Using title to generate slug

        # Call the super method to save the model
        super(Education, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return self.school_name