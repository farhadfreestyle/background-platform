from django.shortcuts import render
from skills.models import Skill
# Create your views here.


def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills/skills.html', {'skills':skills})