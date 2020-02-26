from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from . import forms
from django.views.generic import CreateView
class SignUp(CreateView):
    form_class = forms.UserCreateform
    success_url = reverse_lazy('login')
    template_name= 'account/signup.html'