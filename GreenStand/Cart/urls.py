from django.urls import path
from . import views

app_name = 'Cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<slug:item_slug>/',
        views.cart_add,
        name='cart_add'),
    path('remove/<int:item_id>/',
        views.cart_remove,
        name='cart_remove'),
]