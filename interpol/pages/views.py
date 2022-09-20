from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import CustomUser
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

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'interpol/index.html'
    field = ['name', 'surname', 'email', 'username', 'age', 'password']
