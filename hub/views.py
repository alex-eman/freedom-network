"""
hub/views.py
"""

from django.shortcuts import render

def home(request):
    return render(request, 'hub/home.html')

def about_freenet(request):
    return render(request, 'hub/about_freenet.html')

def about_org(request):
    return render(request, 'hub/about_org.html')

def contact(request):
    return render(request, 'hub/contact.html')

def become_mentor(request):
    return render(request, 'hub/become_mentor.html')

def need_help(request):
    return render(request, 'hub/need_help.html')
