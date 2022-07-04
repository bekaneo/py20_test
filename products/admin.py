from django.contrib import admin
from products.models import Product
from products.models import Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'name', 'description', 'price', 'image', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name',)}
    # list_display = ('name', 'slug')

# admin.site.register(Product)
# admin.site.register(Category)
