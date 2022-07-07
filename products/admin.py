from django.contrib import admin

from products.models import Product, Category, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'name', 'description', 'price', 'image', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['author', 'product', 'text']

# admin.site.register(Product)
# admin.site.register(Category)
