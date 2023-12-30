from django.urls import path, include

from .views import experience, experience_detail

app_name = 'experiences'

urlpatterns = [

    path('experience', experience, name='experiences'),
    path('experience/<slug:slug>/', experience_detail, name='experience_detail'),
   
]