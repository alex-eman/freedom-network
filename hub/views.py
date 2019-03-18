"""
hub/views.py
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from .forms import ContactForm
from .models import Resource

# Render specific homepage dependent on user type
@login_required
def home(request):
    if request.user.is_staff:

        mentor = User.objects.filter(username=request.user.username)

        context = {
            'user': mentor[0],
            'mentees': Profile.objects.filter(mentor=mentor[0])
        }

        return render(request, 'hub/dashboard.html', context)
    else:
        return render(request, 'hub/home.html')

# Render About Freedom Network page
def about_freenet(request):
    return render(request, 'hub/about_freenet.html')

# Render About Partner Organization page
def about_org(request):
    return render(request, 'hub/about_org.html')


def contact(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            content = form.cleaned_data['message']


    return render(request, 'hub/contact.html', {'form': form})

def become_mentor(request):
    return render(request, 'hub/become_mentor.html')

def need_help(request):
    return render(request, 'hub/need_help.html')

def messages(request):
    if request.user.is_staff:
        
        mentor = User.objects.filter(username=request.user.username)

        context = {
            "message_page": "active",
            'people': Profile.objects.filter(mentor=mentor[0])
        }
    
    else:

        mentee = User.objects.filter(username=request.user.username)
        temp = Profile.objects.filter(user=mentee[0])

        context = {
            "message_page": "active",
            'people': Profile.objects.filter(user=temp[0].mentor)
        }

    return render(request, 'hub/messages.html', context)

    # context = {"message_page": "active"}
    # return render(request, 'hub/messages.html', context)

def resources(request):

    res = Resource.objects.all()

    context = {
        "resources_page": "active",
        'resources': res
    }
    return render(request, 'hub/resources.html', context)

def jobs(request):
    context = {"jobs_page": "active"}
    return render(request, 'hub/jobs.html', context)

def forums(request):
    context = {"forums_page": "active"}
    return render(request, 'hub/forums.html', context)
