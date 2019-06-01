from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        return 'Customer id: {id} with username: {username}'.format(id=self.customer_id,username=self.username)

class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    cert_num = models.CharField(max_length=80)

    def __str__(self):
        return 'Farmer id: {id} with username: {username}'.format(id=self.farmer_id,username=self.username)

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__(self):
        return 'Customer id :{customer_id} with order id: {id}'.format(customer_id=self.customer.id,id=self.order_id)

class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    origin = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    count = models.IntegerField()
    quantity = models.IntegerField()
    photo = models.ImageField()

    farmer = models.ForeignKey(Farmer,on_delete = models.CASCADE)

    def __str__(self):
        return 'Item id : {item_id} with price :{price} '.format(item_id=self.item_id,price = self.price)

class OrderItems(models.Model):
    order= models.ForeignKey(Orders,on_delete = models.CASCADE)
    item = models.ForeignKey(Items,on_delete= models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return 'Ordered item with id: {item_id} from order number : {order_id}'.format(item_id=self.item.item_id,\
            order_id=self.order.order_id)

class OrderedBy(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    farmer = models.ForeignKey(Farmer,on_delete = models.CASCADE)

    def __str__(self):
        return 'Customer with id: {customer_id} ordered from farmer with id: {farmer_id}'.format(
                                                                                customer_id=self.customer.customer_id,
                                                                                farmer_id = self.farmer.farmer_id
                                                                                )

