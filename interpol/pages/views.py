from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth import authenticate
from django import forms
from .forms import CustomUserCreationForm


class indexView(TemplateView):
    template_name = 'interpol/index.html'

class indexRuView(TemplateView):
    template_name = 'interpol/indexRu.html'

class aboutView(TemplateView):
    template_name = 'interpol/about.html'

class aboutRuView(TemplateView):
    template_name = 'interpol/aboutRu.html'

class newsView(TemplateView):
    template_name = 'interpol/news.html'

class newsRuView(TemplateView):
    template_name = 'interpol/newsRu.html'

class ErrorView(TemplateView):
    template_name = 'interpol/message-box.html'

class RegisterView(CreateView):
    template_name = 'interpol/index.html'
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        age = request.POST.get('age')
        secret = request.POST.get('secret code')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if(password == password2):
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, age=age, password=password)
            print('гуд')
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return

