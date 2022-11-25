from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse('<h1>Thanks for Contract with us</h1>')
    return render(request, 'contact.html')
