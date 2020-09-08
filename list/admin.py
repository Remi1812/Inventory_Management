from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(raw_master)
admin.site.register(product_master)
admin.site.register(squ_master)
admin.site.register(vendor_master)
admin.site.register(purchase)
admin.site.register(ledger)
admin.site.register(customer_master)
admin.site.register(sale)
