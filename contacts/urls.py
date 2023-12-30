from django.urls import path, include

from .views import contacts
app_name = 'contacts'

urlpatterns = [
    path('contacts', contacts, name='contacts')
   
]