from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from datetime import datetime

# Create your views here.

def home(request):
    date = datetime.now()
    if request.method=='POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Message sent successfully')
            
    else:
        fm = ContactForm()
    return render(request, 'core/home.html', {'form':fm, 'date':date})

# def contact_me(request):
#     if request.method=='POST':
#         fm = ContactForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#             messages.success(request, 'Message sent successfully')
#     else:
#         fm = ContactForm()
#     return render(request, 'core/contact.html', {'form':fm})