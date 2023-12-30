from django.shortcuts import render, get_object_or_404
from education.models import Education
# Create your views here.
def education(request):
    education = Education.objects.all()
    return render(request, 'education/education.html', {'education':education})

def education_details(request, slug):
    detail = get_object_or_404(Education, slug=slug)
    return render(request, 'education/education-detail.html', {'detail':detail})