from django.urls import path
from . import views
from django.views import View
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.home, name='home'),
path('register/', views.register, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)