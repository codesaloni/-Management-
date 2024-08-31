from django.contrib import admin

from .models import Product
from .models import staff

from .models import buyer
from .models import Seller

class productAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity')
    list_filter=['name',]

class staffAdmin(admin.ModelAdmin):
    list_display=('staff_name','staff_number','staff_email')



class buyerAdmin(admin.ModelAdmin):
    list_display=('buyer_name','buyer_number','buyer_address','buyer_email','product','buyer_pincode','product_quantity')


class sellerAdmin(admin.ModelAdmin):
    list_display=('seller_name','seller_email','seller_address','seller_number','seller_quantity','Buyer')

admin.site.register(Product,productAdmin)
admin.site.site_header="Management System"
admin.site.register(staff,staffAdmin)

admin.site.register(buyer,buyerAdmin)
admin.site.register(Seller,sellerAdmin)
