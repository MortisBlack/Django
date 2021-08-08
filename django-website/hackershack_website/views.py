from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(
        request=request, 
        template_name="index.html", 
        context={})

def about(request):
    return render(
        request=request, 
        template_name="about.html", 
        context={})

def contact(request):
    return render(
        request=request, 
        template_name="contact.html", 
        context={})

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
