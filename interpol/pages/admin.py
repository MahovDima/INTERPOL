from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, SecretCode, WantedPerson, Role

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['id','username', 'first_name', 'last_name', 'email', 'role']
    model = CustomUser

class SecretCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'role']
    model = SecretCode

class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'role']
    model = Role

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SecretCode, SecretCodeAdmin)
admin.site.register(WantedPerson)
admin.site.register(Role, RoleAdmin)