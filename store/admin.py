from django.contrib import admin

from store.models import Category, Product




class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    
    
class ProductAdmin(admin.ModelAdmin):
    prepopuleted_fields = {"slug":("name",)}
    



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)