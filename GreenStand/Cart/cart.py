from decimal import Decimal
from django.conf import settings
from Shop.models import Item

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item, quantity=1, update_quantity=False):
        item_id = str(item.item_id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 0,
                                    'unit_price': str(item.unit_price)}
        if update_quantity: 
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, item):
        item_id = str(item.item_id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def __iter__(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        cart = self.cart.copy()
        for item in items:
            cart[str(item.item_id)]['item'] = item
        
        for item in cart.values():
            item['unit_price'] = Decimal(item['unit_price'])
            item['total_price'] = item['unit_price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def total_price(self):
        return sum(Decimal(item['unit_price'])*item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
        