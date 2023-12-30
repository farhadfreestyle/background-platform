from django.urls import path, include
from .views import skills


app_name = 'skills'

urlpatterns = [

   path('skills', skills, name='skills')
]