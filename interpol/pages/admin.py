from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, SecretCode, WantedPerson, Comment

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['id','username', 'first_name', 'last_name', 'email', 'age', 'post', 'warnings']
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SecretCode)
admin.site.register(WantedPerson)
admin.site.register(Comment)