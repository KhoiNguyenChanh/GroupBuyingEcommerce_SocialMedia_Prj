from django.contrib import admin
from .models import User, Category, Product, Tag

#custom admin temp
#rember, common admin is static, do rewrite it when making changes, or else, errors
class CommonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_editable = ['name']
    search_fields = ['name']
    list_filter = ['id', 'name']

class CategoryAdmin(CommonAdmin):
    pass

class ProductAdmin(CommonAdmin):
    list_display = ['pk', 'name', 'image']

class TagAdmin(CommonAdmin):
    pass


class UserAdmin(CommonAdmin):
    list_display = ['pk', 'username']
    list_editable = ['username']
    search_fields = ['username']
    list_filter = ['id', 'username']


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)

