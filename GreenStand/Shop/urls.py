from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.item_list, name='item_list'),
    path('catalog/<slug:category_slug>/', views.item_list,
        name='item_list_by_category'),
    path('<int:id>/<slug:slug>/', views.item_detail,
        name='item_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
