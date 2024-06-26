from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return  self.name 
    
    
class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return  self.name
    
    
class Color(models.Model):
    name = models.CharField(max_length=200)
    code =  models.CharField(max_length=50)
    
    def __str__(self):
        return  self.name
    

class Filter_Price(models.Model):
    Filter_Price = (
        ('10000 TO 20000', '1000 TO 20000'),
        ('20000 TO 30000', '20000 TO 30000'),
        ('30000 TO 40000', '30000 TO 40000'),
        ('40000 TO 50000', '40000 TO 50000'),
        ('50000 TO 60000', '50000 TO 60000'),
        ('60000 TO 70000', '60000 TO 70000'),
    )
    price = models.CharField(choices= Filter_Price, max_length=50)
    
    def __str__(self):
        return  self.price
    
    
class Product(models.Model):
    CONDITION = (( 'New','New'),( 'old','old'))
    STOCK = ('In Stock', 'In Stock'), ( 'Out of stock', 'Out of stock')
    STATUS =('Publish','Publish'),('Draft','Draft')
    
    
    
    unique_id = models.CharField(unique= True, max_length=200, null = True, blank = True) 
    images = models.ImageField(upload_to= 'Product_images/img', default= "no-image.jpg")  
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION, max_length=200)
    information = RichTextField(null=True)
    description = RichTextField(null=True)
    stock = models.CharField(choices= STOCK, max_length=200)
    status = models.CharField(choices= STATUS, max_length=200)
    created_date = models.DateTimeField(default= timezone.now)

    categories = models.ForeignKey (Category , on_delete=models.CASCADE)
    brand = models.ForeignKey (Brand , on_delete=models.CASCADE)
    color = models.ForeignKey (Color , on_delete=models.CASCADE)
    filter_price = models.ForeignKey (Filter_Price , on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return  super().save(*args,**kwargs)
    
    def __str__(self):
        return  self.name
    
    

class Image(models.Model):
    image = models.ImageField(upload_to= 'Product_images/img')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Contact_US(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=300)
    massage = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  self.email

class Order(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=300, null=True, blank=True)
    paid = models.BooleanField(default = False, null = True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return  self.user.username
    
class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE, null =True)
    order = models.ForeignKey(Order,on_delete = models.CASCADE, null =True)
    product = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Product_Images/Order_Img')
    Quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length = 1000)
    
    def __str__(self):
        return  self.order.user.username
    
