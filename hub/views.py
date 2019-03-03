"""
hub/views.py
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile

@login_required
def home(request):
    if request.user.is_staff:

        mentor = User.objects.filter(username=request.user.username)

        context = {
            'mentees': Profile.objects.filter(mentor=mentor[0])
        }

        return render(request, 'hub/dashboard.html', context)
    else:
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
