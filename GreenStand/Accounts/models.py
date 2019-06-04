from django.db import models

class Account(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    is_farmer = models.BooleanField(default=False)

    def __str__(self):
        return 'Account id: {id} with username: {username}'.format(id=self.id,username=self.username)