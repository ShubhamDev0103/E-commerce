from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = admin.site.site_title = "N-AIR Admin Pannel"

admin.site.register(Master)
admin.site.register(Profile)
admin.site.register(cart)
admin.site.register(Customer)
admin.site.register(order_place)
admin.site.register(Product)
