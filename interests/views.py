from django.shortcuts import render
from interests.models import Interest
# Create your views here.
def interests(request):
    interests = Interest.objects.all()

    return render(request, 'interests/interests.html', {'interests':interests})