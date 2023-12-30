from django.shortcuts import render
from research.models import Research
# Create your views here.

def research(request):
    research = Research.objects.all()

    return render(request, 'research/research.html', {'research':research})