from django.contrib import admin
from category.models import Category

# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id','category_name','slug','description','cate_image']
    prepopulated_fields = {'slug':('category_name',)}
