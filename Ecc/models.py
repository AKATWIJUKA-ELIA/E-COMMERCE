from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager
from PIL import Image
import random
import string
from django.utils.timezone import now
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

class News_letter(models.Model):
    email = models.EmailField(blank=True,default=None)
    
# class Admin(models.Model):
#       email = models.EmailField(unique=True)
#       username = models.CharField(max_length=100,unique=True)
#       password = models.CharField(max_length=100)
      

class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})
  
class Customers(AbstractBaseUser , PermissionsMixin):
      
      username = models.CharField(max_length=100,unique=True)
      Customer_id = models.CharField(max_length=255,primary_key=True,unique=True)
      def save(self, *args, **kwargs):
        if not self.Customer_id:  # Only generate if no ID is set
            # Get the last object inserted to determine the next ID
            last_object = Customers.objects.all().order_by('Customer_id').last()

            if last_object:
                # Extract the number from the last ID and increment it
                last_id = last_object.Customer_id
                number = int(last_id[5:]) + 1
                new_id = f'CUST-{str(number).zfill(3)}'
            else:
                new_id = 'CUST-001'  # Start with 'fxx001' if no object exists
            
            self.Customer_id = new_id

        super(Customers, self).save(*args, **kwargs)
      email = models.EmailField(blank=True, default=None)
      password = models.CharField(max_length=255,)
      phone_number = models.CharField(max_length=20, blank=True, default=None)
      reset_token = models.CharField(max_length=255, blank=True, null=True)
      reset_token_expires = models.DateTimeField(blank=True, null=True)
      address = models.CharField(max_length=255, blank=True, default=None)
      USERNAME_FIELD = 'username'  # or whatever field you want to use as the username
      REQUIRED_FIELDS = ['email', 'password','phone_number']
      objects = CustomUserManager()

     
class Products(models.Model):
      product_id = models.CharField(max_length=10, unique=True, primary_key=True, editable=False)
      def save(self, *args, **kwargs):
        # Assign a random string only if product_id is not already set
        if not self.product_id:
            while True:
                random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))  # 10-character random string
                if not Products.objects.filter(product_id=random_id).exists():  # Ensure uniqueness
                    self.product_id = random_id
                    break
        super().save(*args, **kwargs)

      product_name = models.CharField(max_length=255)
      product_price = models.DecimalField(max_digits=100, decimal_places=2)
      product_description = models.CharField(max_length=255)
      product_cartegory = models.CharField(max_length=255,default='breakfast')
      product_condition = models.CharField(max_length=255,default='None')
      product_owner = models.ForeignKey(to=Customers,on_delete=models.CASCADE,default=None)
      Created_At = models.DateTimeField(default=now)
      Approved = models.BooleanField(blank=True, default=False)

class Upload_Images(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    product_image = CloudinaryField('image', blank=True,transformation=[
            {'width': 1156, 'height': 765, 'crop': 'fill'}  # Resize & crop to fit
        ], null=True)  # Cloudinary handles storage
#     def __str__(self):
        # return f"Image for {self.product.name}"

#     def save(self, *args, **kwargs):
#         # Check if the uploaded file is a valid image
#         if self.product_image and hasattr(self.product_image, 'file'):
#             allowed_types = ['image/jpeg', 'image/png', 'image/gif']
#             if self.product_image.file.content_type not in allowed_types:
#                 raise ValueError('Only JPG, JPEG, PNG, and GIF image files are allowed')

#         # Save the image to Cloudinary
#         super().save(*args, **kwargs)  

#     def get_resized_image_url(self):
#         """Returns a resized image URL using Cloudinary transformations."""
#         if self.product_image:
#             return f"{self.product_image.url}?w=1156&h=765&c=fill&q=80"  # Resize & compress
#         return ""
# Signal to delete the image file when the Upload_Images instance is deleted
# @receiver(post_delete, sender=Upload_Images)
# def delete_image_file(sender, instance, **kwargs):
#     if instance.product_image:
#         # Delete the image file from storage
#         if os.path.isfile(instance.product_image.path):
#             os.remove(instance.product_image.path)
        
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True, unique=True)
    cart_user = models.ForeignKey(to=Customers, on_delete=models.CASCADE)  # Link each cart to a customer (user)
    cart_product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='cart_items')  # Link each cart to a product
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product in the cart
    cart_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)  # Total price for this cart item

    def save(self, *args, **kwargs):
        # Update cart amount based on product price and quantity
        self.cart_amount = self.cart_product.product_price * self.quantity
        super(Cart, self).save(*args, **kwargs)

    def __str__(self):
        return f"Cart {self.cart_id} | User: {self.cart_user.username} | Product: {self.cart_product.product_name} | Quantity: {self.quantity}"
      
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_user = models.ForeignKey(Customers, on_delete=models.CASCADE)  # The customer who placed the order
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="orders")  # Link to the cart(s) associated with the order
    order_date = models.DateTimeField(auto_now_add=True)  # When the order was placed
    shipping_address = models.CharField(max_length=1024,null=True)  # Shipping address
    payment_status = models.CharField(max_length=255,null=True, choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed')], default='pending')
    order_status = models.CharField(max_length=255,null=True, choices=[('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='processing')
    total_amount = models.DecimalField(max_digits=10,null=True, decimal_places=2)  # Total amount for the order

    def __str__(self):
        return f"Order {self.order_id} | User: {self.order_user.username} | Status: {self.order_status}"
      
    def calculate_total_amount(self):
        # Sum the total amount for all products in the cart(s) related to the order
        self.total_amount = self.cart.cart_amount
        self.save()
        
class Payments(models.Model):
      payment_id = models.CharField(max_length=255,primary_key=True)
      customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
      order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
      payment_date = models.DateTimeField()
      Amount = models.DecimalField(decimal_places=2,max_digits=10)
      
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    title = models.CharField(max_length=255)

class Categories(models.Model):
        category_id = models.AutoField(primary_key=True)
        category_name = models.CharField(max_length=255)