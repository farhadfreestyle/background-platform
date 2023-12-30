from django.urls import path, include
from .views import education, education_details

app_name = 'education'

urlpatterns = [

    path('education', education, name='education'),
    # path('education-detail')
     path('education/<slug:slug>/', education_details, name='education_detail'),

   
]