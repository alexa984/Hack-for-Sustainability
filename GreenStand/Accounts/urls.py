from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register_as/', views.register_as, name='register_as'),
    path('register/<user_type>', views.register, name='register' ),
]
