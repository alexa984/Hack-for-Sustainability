from django.views import View
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
