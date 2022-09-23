from django.views.generic import TemplateView, CreateView, ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import CustomUser, SecretCodes
from django.contrib.auth import authenticate
from django import forms
from .forms import CustomUserCreationForm
import random


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

class profileView(ListView):
    template_name = 'interpol/profile.html'
    model = SecretCodes

class profileRuView(ListView):
    template_name = 'interpol/profileRu.html'
    model = SecretCodes

class SecretCodesView(CreateView):
    def post(self, request, *args, **kwargs):
        count = int(request.POST.get('codeCount'))
        chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        for c in range(count):
            secretCode = SecretCodes()
            secretCode.code = ''
            for i in range(4):
                for j in range(4):
                    secretCode.code += chars[random.randint(0, 61)]
                if i < 3:
                    secretCode.code += '-'
            secretCode.save()
        return HttpResponseRedirect(reverse_lazy('en/profile'))

class RegisterView(CreateView):
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        secretCode = request.POST.get('secret code')
        age = request.POST.get('age')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if(SecretCodes.objects.filter(code=secretCode)):
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, post='staffer', email=email, username=username, age=age, password=password)
            SecretCodes.objects.filter(code=secretCode).delete()
        else:
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, age=age, password=password)

        return HttpResponseRedirect(reverse_lazy('home'))

