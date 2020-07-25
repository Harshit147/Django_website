from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    def _str_(self):
        return self.product_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, default="")
    phone = models.CharField(max_length=10, default="")
    desc = models.CharField(max_length=500, default="")



    def __str__(self):
        return self.name
class Orders(models.Model):
    Order_Id =models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=2000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address = models.CharField(max_length=110)
    city = models.CharField(max_length=110)
    state = models.CharField(max_length=100)
    zip_code= models.CharField(max_length=10)
