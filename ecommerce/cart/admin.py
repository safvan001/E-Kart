from django.contrib import admin

from cart.models import Cart,Account,Orders

admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Account)

# Register your models here.
