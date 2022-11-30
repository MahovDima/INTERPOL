from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from .models import CustomUser, SecretCode, WantedPerson, Role
from django.contrib.auth import authenticate, login
from django import forms
from .forms import CustomUserCreationForm
import datetime
import random


class indexView(TemplateView):
    template_name = 'interpol/index.html'

    def get_context_data(self, **kwargs):
        context = super(indexView, self).get_context_data(**kwargs)
        if self.request.GET:
            if self.request.GET.get('errorSignIn'):
                context['errorSignIn'] = self.request.GET.get('errorSignIn')
            elif self.request.GET.get('errorSignUp'):
                context['errorSignUp'] = self.request.GET.get('errorSignUp')
        return context
class indexRuView(TemplateView):
    template_name = 'interpol/indexRu.html'

    def get_context_data(self, **kwargs):
        context = super(indexRuView, self).get_context_data(**kwargs)
        if self.request.GET:
            if self.request.GET.get('errorSignIn'):
                context['errorSignIn'] = self.request.GET.get('errorSignIn')
            elif self.request.GET.get('errorSignUp'):
                context['errorSignUp'] = self.request.GET.get('errorSignUp')
        return context

class aboutView(TemplateView):
    template_name = 'interpol/about.html'

    def get_context_data(self, **kwargs):
        context = super(aboutView, self).get_context_data(**kwargs)
        if self.request.GET:
            if self.request.GET.get('errorSignIn'):
                context['errorSignIn'] = self.request.GET.get('errorSignIn')
            elif self.request.GET.get('errorSignUp'):
                context['errorSignUp'] = self.request.GET.get('errorSignUp')
        return context

class aboutRuView(TemplateView):
    template_name = 'interpol/aboutRu.html'

    def get_context_data(self, **kwargs):
        context = super(aboutRuView, self).get_context_data(**kwargs)
        if self.request.GET:
            if self.request.GET.get('errorSignIn'):
                context['errorSignIn'] = self.request.GET.get('errorSignIn')
            elif self.request.GET.get('errorSignUp'):
                context['errorSignUp'] = self.request.GET.get('errorSignUp')
        return context

class newsView(TemplateView):
    template_name = 'interpol/news.html'

    def get_context_data(self, **kwargs):
        context = super(newsView, self).get_context_data(**kwargs)
        if self.request.GET:
            if self.request.GET.get('errorSignIn'):
                context['errorSignIn'] = self.request.GET.get('errorSignIn')
            elif self.request.GET.get('errorSignUp'):
                context['errorSignUp'] = self.request.GET.get('errorSignUp')
        return context

class newsRuView(TemplateView):
    template_name = 'interpol/newsRu.html'

    def get_context_data(self, **kwargs):
        context = super(newsRuView, self).get_context_data(**kwargs)
        if self.request.GET:
            if self.request.GET.get('errorSignIn'):
                context['errorSignIn'] = self.request.GET.get('errorSignIn')
            elif self.request.GET.get('errorSignUp'):
                context['errorSignUp'] = self.request.GET.get('errorSignUp')
        return context

class profileView(ListView):
    template_name = 'interpol/profile.html'
    model = SecretCode
    def get_context_data(self, **kwargs):
        context = super(profileView, self).get_context_data(**kwargs)
        if self.request.GET:
            if self.request.GET.get('errorSignIn'):
                context['errorSignIn'] = self.request.GET.get('errorSignIn')
            elif self.request.GET.get('errorSignUp'):
                context['errorSignUp'] = self.request.GET.get('errorSignUp')
        return context

class profileRuView(ListView):
    template_name = 'interpol/profileRu.html'
    model = SecretCode

    def get_context_data(self, **kwargs):
        context = super(profileRuView, self).get_context_data(**kwargs)
        context['roles'] = Role.objects.all()
        if self.request.GET:
            if self.request.GET.get('errorSignIn'):
                context['errorSignIn'] = self.request.GET.get('errorSignIn')
            elif self.request.GET.get('errorSignUp'):
                context['errorSignUp'] = self.request.GET.get('errorSignUp')
        return context

class wantedView(ListView):
    model = WantedPerson
    template_name = 'interpol/wanted.html'

    def get_context_data(self, **kwargs):
        context = super(wantedView, self).get_context_data(**kwargs)
        if self.request.GET:
            if self.request.GET.get('errorSignIn'):
                context['errorSignIn'] = self.request.GET.get('errorSignIn')
            elif self.request.GET.get('errorSignUp'):
                context['errorSignUp'] = self.request.GET.get('errorSignUp')
        return context

class wantedRuView(ListView):
    model = WantedPerson
    template_name = 'interpol/wantedRu.html'

    def get_context_data(self, **kwargs):
        context = super(wantedRuView, self).get_context_data(**kwargs)
        if self.request.GET:
            if self.request.GET.get('errorSignIn'):
                context['errorSignIn'] = self.request.GET.get('errorSignIn')
            elif self.request.GET.get('errorSignUp'):
                context['errorSignUp'] = self.request.GET.get('errorSignUp')
        return context


class requestView(ListView):
    model = WantedPerson
    template_name = 'interpol/request.html'


class requestRuView(ListView):
    model = WantedPerson
    template_name = 'interpol/requestRu.html'

def updateRequest(request,pk):
    requestPerson = WantedPerson.objects.get(pk=pk)
    requestPerson.isPublished = True
    requestPerson.save()
    return HttpResponseRedirect(reverse_lazy('en/request'))

def deleteRequest(request,pk):
    requestPerson = WantedPerson.objects.get(pk=pk)
    requestPerson.delete()
    return HttpResponseRedirect(reverse_lazy('en/request'))

class editRequest(UpdateView):
    model = WantedPerson
    fields = ['name', 'age', 'briefInfo', 'detailInfo']
    template_name = 'interpol/request_edit.html'
    success_url = reverse_lazy('en/request')

    def post(self, request, *args, **kwargs):
        person = WantedPerson.objects.get(pk=self.kwargs.get('pk'))
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.briefInfo = request.POST.get('briefInfo')
        person.detailInfo = request.POST.get('detailInfo')
        person.save()
        return HttpResponseRedirect(reverse_lazy('en/request'))


class WantedPersonsView(CreateView):
    def post(self, request, *args, **kwargs):
        person = WantedPerson()
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.briefInfo = request.POST.get('briefInfo')
        if 'photo' in request.FILES:
            person.photo = request.FILES['photo']
        person.detailInfo = request.POST.get('detailInfo')
        person.save()
        return HttpResponseRedirect(reverse_lazy('en/wanted'))
class SecretCodesView(CreateView):
    def post(self, request, *args, **kwargs):
        if request.POST.get('codeCount') == '':
            return HttpResponseRedirect(reverse_lazy('en/profile'))
        count = int(request.POST.get('codeCount'))
        post = int(request.POST.get('post'))
        chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        for c in range(count):
            secretCode = SecretCode()
            secretCode.code = ''
            for i in range(4):
                for j in range(4):
                    secretCode.code += chars[random.randint(0, 61)]
                if i < 3:
                    secretCode.code += '-'
            secretCode.role = Role.objects.get(id=post)
            secretCode.save()
        return HttpResponseRedirect(reverse_lazy('en/profile'))

class RegisterView(CreateView):
    def post(self, request, *args, **kwargs):
        errors = 0
        get = None
        if request.POST.get('password2') or request.POST.get('password2') == '':
            requiredFields = ['first_name', 'last_name', 'email', 'username', 'password1']
            for field in requiredFields:
                if request.POST[field] == '':
                    errors += 1
                    get = '?errorSignUp=empty-field'
                    break
            else:
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                username = request.POST.get('username')
                secretCode = request.POST.get('secret code')
                password = request.POST.get('password1')
                password2 = request.POST.get('password2')
                if password != password2:
                    errors += 1
                    get = '?errorSignUp=password-validation'
                if CustomUser.objects.filter(email=email):
                    errors += 1
                    get = '?errorSignUp=email-validation'
                if CustomUser.objects.filter(username=username):
                    errors += 1
                    get = '?errorSignUp=username-validation'
                if not SecretCode.objects.filter(code=secretCode):
                    errors += 1
                    get = '?errorSignUp=code-validation'
            if not errors:
                if SecretCode.objects.filter(code=secretCode, role=Role.objects.get(role='Interpol staff')):
                    user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, role=Role.objects.get(id=4), email=email, username=username, password=password)
                    SecretCode.objects.filter(code=secretCode).delete()
                elif SecretCode.objects.filter(code=secretCode,role=Role.objects.get(role='police staff')):
                    user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, role=Role.objects.get(id=3), email=email, username=username, password=password)
                    SecretCode.objects.filter(code=secretCode).delete()
                else:
                    print("нет")
        else:
            requiredFields = ['username', 'password']
            for field in requiredFields:
                if request.POST[field] == '':
                    get = '?errorSignIn=empty-field'
                    break
            else:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    print(type(request.user.role))
                else:
                    get = "?errorSignIn=undefinedUser"

        if get:
            if '?' in request.META.get('HTTP_REFERER'):
                return HttpResponseRedirect(request.META.get('HTTP_REFERER').split('?', 1)[0] + get)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER') + get)
        else:
            if '?' in request.META.get('HTTP_REFERER'):
                return HttpResponseRedirect(request.META.get('HTTP_REFERER').split('?', 1)[0])
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))