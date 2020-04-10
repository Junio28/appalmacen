from django.contrib import admin

# Register your models here.
from apps.products.models import ProductType, Product

class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ('created', 'updated') #No permite edicion de create y update
    list_display = ('name', 'quantity', 'price', 'description', 'mark', 'product_types')
    ordering = ('price','name','mark','product_types') # En caso que sea una sola ordering('column',)


admin.site.register(ProductType)
admin.site.register(Product, ProductAdmin)
