from django.shortcuts import render
from website.forms import ContactForm
from django.contrib import messages
# Create your views here.

def index_view(request):
    return render(request , 'website/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS , 'your ticket submited successfully')
        else:
            messages.add_message(request , messages.ERROR , 'your ticket didnt submited')
    form = ContactForm()
    return render(request , 'website/contact.html' , {'form' : form})

def about_view(request):
    return render(request , 'website/about.html')