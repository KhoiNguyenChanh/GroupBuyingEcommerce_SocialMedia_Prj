from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, Category, Product, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# custom admin temp
# rember, common admin is static, do rewrite it when making changes, or else, errors
class CommonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']

    #dung css tao mau cho cac trang details
    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


class CategoryAdmin(CommonAdmin):
    list_editable = ['name']

#de upload anh thong qua richtextfield
class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Product
        fields = '__all__'

class TagInlineAdmin(admin.TabularInline):
    model = Product.tags.through

#nho gan static vao truoc cho upload, cai day thao tac thu cong de them vao static
class ProductAdmin(CommonAdmin):
    list_display = ['pk', 'name', 'price', 'img', 'created_date', 'updated_date', 'category', 'active']
    search_fields = ['name', 'category']
    readonly_fields = ['img']
    inlines = [TagInlineAdmin]
    form = ProductForm
    def img(self, product):
        if product:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'
                    .format(url=product.image.name)
            )




class TagAdmin(CommonAdmin):
    list_editable = ['name']


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
