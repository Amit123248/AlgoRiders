from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Img(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='test_imgs')

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    add = models.TextField(default="")
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.name
    
class category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cat_img')
    description = models.TextField()

    def __str__(self):
        return self.name
    
class product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_img')
    description = models.TextField()
    stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name    
    
class order(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    pro = models.ForeignKey(product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    add = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    total_price = models.PositiveIntegerField()
    payment_type = models.CharField(max_length=20)
    payment_id = models.CharField(max_length=50)
    dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
    
class cart(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    pro = models.ForeignKey(product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    order_id = models.PositiveIntegerField(max_length=50, default="0")    

    def __str__(self):
        return str(self.user)