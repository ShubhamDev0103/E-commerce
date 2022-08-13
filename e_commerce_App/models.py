from msilib.schema import Class
from sre_constants import CATEGORY
from telnetlib import STATUS
from unicodedata import name
from django.db import models


class Master(models.Model):
    Email = models.EmailField(max_length=10)
    Password = models.CharField(max_length=8)
    isactive = models.BooleanField(default=False)

    def __str__(self):
        return self.Email

    class Meta:
        db_table = "master"

class Profile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    Fullname = models.CharField(max_length=25, default="")
    Address = models.CharField(max_length=100, default="")
    Mobile = models.IntegerField(default=0)
    City = models.CharField(max_length=10, default="")
    State = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.Fullname

    class Meta:
        db_table = "profile"

STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Orissa', 'Orissa'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Other', 'Other')
)



CATEGORY_CHOICES = (
    ('M', 'MEN'),
    ('F', 'FEMALE'),
    ('K', 'KIDS')
)

SHOP_CATEGORY = (

    # boys category
    ('MS', 'Men-Shoes'),
    ('MT', 'Men-Tops'),
    ('MB', 'Men-Bottom'),
    ('CC', 'Men-Casual'),
    ('G', 'Men-gym'),
    # woman category
    ('WS', 'Women-Shoes'),
    ('WT', 'Women-Tops'),
    ('WB', 'Women-Bottom'),
    # kids category
    ('KT','kids_t-shirt'),
    ('KG','kids-gear'),
    ('KW','kids-watch'),
    ('KS','kids-shoes'),
)


class Product(models.Model):
    # Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default=" ")
    selling_price = models.IntegerField(default=" ")
    discount_price = models.IntegerField(default="")
    description = models.TextField()
    brand = models.CharField(max_length=10, default="")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    subcategory = models.CharField(max_length=50, choices = SHOP_CATEGORY)
    shoes_img = models.ImageField(upload_to='media_photo')
    # Size = models.PositiveSmallIntegerField(default=1)


    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(Master, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=10)
    status = models.CharField(choices=STATE_CHOICES, max_length=20)


    def __str__(self):
        return str(self.id)

class cart(models.Model):
    user = models.ForeignKey(Master, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default="1")
    Size = models.PositiveSmallIntegerField(default=1)

    # delivery_charges = models.IntegerField(default=80)
    cart_c = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

    def __str__(self):
        return str(self.user)
    
STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On_The_Way', 'On_The_Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)


class order_place(models.Model):
    user = models.ForeignKey(Master, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default="1")
    # delivery_charges = models.IntegerField(default=80)
    # order_date = models.DateField(auto_now_add=True)
    status = models.CharField( max_length=20, choices=STATUS_CHOICES, default="Pending")
