from django.shortcuts import render, get_object_or_404
from experience.models import Experience
# Create your views here.
def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'experience/experiences.html', {'experiences':experiences})


def experience_detail(request, slug):
    detail = get_object_or_404(Experience, slug=slug)
    return render(request, 'experience/experience-detail.html', {'detail':detail})