from django.contrib import admin
from order.models import ShopCart
# Register your models here.
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','product','price','quantity','amount']
    list_filter = ['user']

# TODO admin.site.register(ShopCart,ShopCartAdmin)
