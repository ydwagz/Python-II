from django.contrib import admin
from .models import User, Profile, Products, Carts, Payment, System, ProductsHistory

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Products)
admin.site.register(Carts)
admin.site.register(Payment)
admin.site.register(System)
admin.site.register(ProductsHistory)
