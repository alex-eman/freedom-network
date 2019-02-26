"""
hub/urls.py
"""

from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='hub-home'),
    path('about_freenet/', views.about_freenet, name='hub-about_freenet'),
    path('about_org/', views.about_org, name='hub-about_org'),
    path('contact/', views.contact, name='hub-contact'),
    path('become_mentor/', views.become_mentor, name='hub-become_mentor'),
    path('need_help/', views.need_help, name='hub-need_help'),

]