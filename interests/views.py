from django.shortcuts import render
from interests.models import Interest
# Create your views here.
def interests(request):
    interests = Interest.objects.all().order_by('interest_name')

    return render(request, 'interests/interests.html', {'interests':interests})