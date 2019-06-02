from django.urls import path
from . import views
from django.views import View
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/<user_type>/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('register_as/', views.register_as, name='register_as')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
