from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Shop.models import Item
from .cart import Cart
from .forms import CartAddItemForm

@require_POST
def cart_add(request, slug_item):
    cart = Cart(request)
    item = get_object_or_404(Item, slug=slug_item)
    form = CartAddItemForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
    
    return redirect(request.META.get('HTTP_REFERER'))
    

def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)

    return redirect('Cart:cart_detail')

def cart_detail(request):
    template = 'detail.html'
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddItemForm(
                            initial={'quantity': item['quantity'], 'update': True})
    return render(request, template, {'cart': cart})

def item_detail(request, item_id, slug):
    template = 'Shop/template/detail.html'
    product = get_object_or_404(Item, id=item_id, slug=slug,  available=True)
    cart_item_form = CartAddItemForm()
    return render(request, template, {'product': product,'cart_item_form': cart_item_form})