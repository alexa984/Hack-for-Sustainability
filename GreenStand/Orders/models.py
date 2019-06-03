from django.db import models
from Shop.models import Item

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', '-updated',)

    def __str__(self):
        return 'Order with id: {}'.format(self.id)

    def total_order_price(self):
        return sum(item.total_price() for item in self.items.all())

class OrderItem(models.Model):
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='order_items', on_delete=models.CASCADE)

    def __str__(self):
        return 'Order item with id: {}'.format(self.id)

    def total_price(self):
        return self.unit_price * self.quantity