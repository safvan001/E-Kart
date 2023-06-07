from django.contrib import admin

from shop.models import Category,Product
class Categoryadmin(admin.ModelAdmin):
    list_display=['name','slug',]
    prepopulated_fields ={'slug':('name',)}


admin.site.register(Category,Categoryadmin)

class Productadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug', ]

admin.site.register(Product,Productadmin)

# Register your models here.
