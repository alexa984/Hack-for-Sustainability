from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from Cart.cart import Cart

def order_create(request):
    template = '.html'
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        item=item['item'],
                                        unit_price=item['unit_price'],
                                        quantity=item['quantity'])
            cart.clear()
            return render(request, template, {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, template, {'cart': cart, 'form': form})