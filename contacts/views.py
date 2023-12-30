from django.shortcuts import render
from contacts.models import Contact
# Create your views here.
def contacts(request):
    contacts = Contact.objects.first()
    return render(request, 'contacts/contacts.html', {'contacts':contacts})