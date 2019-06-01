from django.urls import path
from . import views
from django.views import View

urlpatterns = [
path('', views.home, name='home'),
path('register/', views.register, name='register')
]