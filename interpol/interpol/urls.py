from django.contrib import admin
from django.urls import path, include,re_path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.indexView.as_view(), name="home"),
    path('ru/home/', views.indexRuView.as_view(), name="ru/home"),

    path('en/about/', views.aboutView.as_view(), name="en/about"),
    path('ru/about/', views.aboutRuView.as_view(), name="ru/about"),

    path('en/news/', views.newsView.as_view(), name="en/news"),
    path('ru/news/', views.newsRuView.as_view(), name="ru/news"),

    path('en/profile/', views.profileView.as_view(), name='en/profile'),
    path('ru/profile/', views.profileRuView.as_view(), name='ru/profile'),

    re_path(r'^codeGenerate/', views.SecretCodesView.as_view(), name='codeGenerate'),

    path('', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register'),
    #re_path(r'$error/', views.ErrorView.as_view(), name='error')
]
