from django.contrib import admin

# Register your models here.
from education.models import Education

admin.site.register(Education)

class EducationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('school_name',)}