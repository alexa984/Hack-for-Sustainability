from django.db import models

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
        return 'Item id : {item_id} with price :{price} '.format(item_id=self.item_id,price = self.unit_price)
