from django.db import models
# from django.contrib.auth.models import User

# class Customer(User):
#     # customer_id = models.AutoField(primary_key=True)
#     # username = models.CharField(max_length=50)
#     # password = models.CharField(max_length=200)
#     # first_name = models.CharField(max_length=20)
#     # last_name = models.CharField(max_length=20)
#     address = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     # email = models.CharField(max_length=50)

#     def __str__(self):
#         return 'Customer id: {id} with username: {username}'.format(id=self.id,username=self.username)

# class Farmer(User):
#     # farmer_id = models.AutoField(primary_key=True)
#     # username = models.CharField(max_length=50)
#     # password = models.CharField(max_length=200)
#     # first_name = models.CharField(max_length=20)
#     # last_name = models.CharField(max_length=20)
#     address = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     # email = models.CharField(max_length=50)
#     certification_number = models.CharField(max_length=80)

#     def __str__(self):
#         return 'Farmer id: {id} with username: {username}'.format(id=self.id,username=self.username)

# class Orders(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     date = models.DateTimeField()
#     customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

#     def __str__(self):
#         return 'Customer id :{customer_id} with order id: {id}'.format(customer_id=self.customer.id,id=self.order_id)

class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    producer = models.CharField(max_length=100)
    producer_certification_number = models.CharField(max_length=50) 
    origin = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=5,decimal_places=2)
    unit_quantity = models.IntegerField()
    photo = models.ImageField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return 'Item id : {item_id} with price :{price} '.format(item_id=self.item_id,price = self.price)

# class OrderItems(models.Model):
#     order= models.ForeignKey(Orders,on_delete = models.CASCADE)
#     item = models.ForeignKey(Items,on_delete= models.CASCADE)
#     quantity = models.IntegerField()

#     def __str__(self):
#         return 'Ordered item with id: {item_id} from order number : {order_id}'.format(item_id=self.item.item_id,\
#             order_id=self.order.order_id)

# class OrderedBy(models.Model):
#     customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
#     farmer = models.ForeignKey(Farmer,on_delete = models.CASCADE)

#     def __str__(self):
#         return 'Customer with id: {customer_id} ordered from farmer with id: {farmer_id}'.format(
#                                                                                 customer_id=self.customer.id,
#                                                                                 farmer_id = self.farmer.id
#                                                                                 )

