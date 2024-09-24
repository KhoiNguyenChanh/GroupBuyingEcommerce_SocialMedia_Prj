from django.contrib import admin
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe

from . import dao
from .models import User, Category, Product, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django.urls import path
from django.urls import reverse
from django.utils.html import format_html

# custom admin temp
class GroupBuyingAdminSite(admin.AdminSite):
    # Custom admin page title
    site_header = "HỆ THỐNG QUẢN TRỊ DỮ LIỆU"
    site_title = "Quản trị hệ thống ứng dụng TMDT"
    index_title = "Chào mừng đến với trang quản trị"

    def get_urls(self):
        return [
            path('product-stats/', self.stats_view, name='product-stats')
        ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats.html', {
            'stats': dao.count_products_by_cate()
        })

    # #tao duong dan den trang stats
    # def index(self, request, extra_context=None):
    #     extra_context = extra_context or {}
    #     # Thêm liên kết đến trang thống kê vào extra_context
    #     extra_context['stats_link'] = reverse('admin:product-stats')
    #     return super().index(request, extra_context=extra_context)
admin_site = GroupBuyingAdminSite(name='myapp')


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

#
class UserAdmin(CommonAdmin):
    list_display = ['pk', 'username']
    list_editable = ['username']
    search_fields = ['username']
    list_filter = ['id', 'username']

#call admin.site = groupbuying site
#admin.site = GroupBuyingAdminSite()

# Register your models here.
admin_site.register(User, UserAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Product, ProductAdmin)
admin_site.register(Tag, TagAdmin)











#
#
#
