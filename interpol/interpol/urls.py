from django.contrib import admin
from django.urls import path, include, re_path
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.indexView.as_view(), name="home"),
    path('ru/home', views.indexRuView.as_view(), name="ru/home"),

    path('en/about', views.aboutView.as_view(), name="en/about"),
    path('ru/about', views.aboutRuView.as_view(), name="ru/about"),

    path('en/news', views.newsView.as_view(), name="en/news"),
    path('ru/news', views.newsRuView.as_view(), name="ru/news"),

    path('en/profile', views.profileView.as_view(), name='en/profile'),
    path('ru/profile', views.profileRuView.as_view(), name='ru/profile'),

    path('en/wanted', views.wantedView.as_view(), name='en/wanted'),
    path('ru/wanted', views.wantedRuView.as_view(), name='ru/wanted'),

    path('en/wanted/requests', views.requestView.as_view(), name='en/request'),
    path('ru/wanted/requests', views.requestRuView.as_view(), name='ru/request'),

    path('wanted/requests/<int:pk>-add', views.updateRequest, name='request_add'),
    path('wanted/requests/<int:pk>-delete', views.deleteRequest, name='request_delete'),
    path('wanted/requests/<int:pk>-edit', views.editRequest.as_view(), name='request_edit'),

    re_path(r'^codeGenerate', views.SecretCodesView.as_view(), name='codeGenerate'),
    re_path(r'^wanted', views.WantedPersonsView.as_view(), name='wanted'),


    path('', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register'),
    #re_path(r'$error/', views.ErrorView.as_view(), name='error')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)