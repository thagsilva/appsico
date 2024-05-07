from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required



app_name = 'appsico_app'

urlpatterns = [
    
]