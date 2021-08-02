from django.contrib import admin
from django.db import models
from store.models import Product

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name','slug','description','price','images','stock','is_available','category','created_date','modified_date']
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product,AdminProduct)