from django.urls import path, include

from .views import research

app_name = 'research'

urlpatterns = [
    path('research', research, name='research')
   
]