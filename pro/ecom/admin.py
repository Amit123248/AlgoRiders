from django.contrib import admin
from .models import Student, Img, Registration, cart, category, product, order

# Register your models here.

class student_(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

admin.site.register(Student,student_)

class img_(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

admin.site.register(Img,img_)

class reg_(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mob', 'add', 'password')

admin.site.register(Registration, reg_)

class cat_(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description')

admin.site.register(category, cat_)

class product_(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'category', 'stock')

admin.site.register(product, product_)

class order_(admin.ModelAdmin):
    list_display = ('id', 'pro', 'user', 'qty', 'total_price', 'payment_type', 'payment_id','dt')
admin.site.register(order, order_)

class cart_(admin.ModelAdmin):
    list_display = ('id', 'pro', 'user', 'qty', 'total_price', 'order_id')
admin.site.register(cart, cart_)