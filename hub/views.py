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

def messages(request):
    context = {"message_page": "active"}
    return render(request, 'hub/messages.html', context)

def resources(request):
    context = {"resources_page": "active"}
    return render(request, 'hub/resources.html', context)

def jobs(request):
    context = {"jobs_page": "active"}
    return render(request, 'hub/jobs.html', context)

def forums(request):
    context = {"forums_page": "active"}
    return render(request, 'hub/forums.html', context)