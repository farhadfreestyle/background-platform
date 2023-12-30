from django.shortcuts import render
from home.models import HomePageData

# Create your views here.
def home(request):
    home_data = HomePageData.objects.first()

    return render(request, 'home/home.html', {'home_data':home_data})