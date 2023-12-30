from django.urls import path, include

from .views import interests

app_name = 'interests'

urlpatterns = [

    path('interests', interests, name='interests')
   
]