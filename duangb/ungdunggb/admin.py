from django.contrib import admin
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe

from . import dao
from .models import (
    User, Category, Product, Tag, Customer,ProductReview, Shop,
    ProductReviewAnswer, ProductReviewVoting,CustomerOrder,
    OrderItem, OrderDeliveryStatus, ShippingAddress, Payment,
    GroupBuy, GroupBuyMember, Cart, CartItem, Wishlist,
    Coupon, Post, Comment, PostLike  )
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
    # class Media:
    #     css = {
    #         'all': ('/static/css/style.css',)
    #     }

# CATEGORY
class CategoryAdmin(CommonAdmin):
    list_editable = ['name']
    list_display = ['pk', 'name', 'description', 'active', 'created_date', 'updated_date']
    search_fields = ['name', 'description']
    list_filter = ['active', 'created_date']

# PRODUCT
#de upload anh thong qua richtextfield, THAY DOI FORM A :))
class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Product
        fields = '__all__'

# TAG INLINE
class TagInlineAdmin(admin.TabularInline):
    model = Product.tags.through

#nho gan static vao truoc cho upload, cai day thao tac thu cong de them vao static
class ProductAdmin(CommonAdmin):
    list_display = ['pk', 'name', 'max_price', 'img', 'created_date', 'updated_date', 'category', 'active']
    search_fields = ['name', 'category']
    readonly_fields = ['img']


    inlines = [TagInlineAdmin]
    form = ProductForm
    # PROD IMAGE
    def img(self, product):
        if product:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'
                    .format(url=product.image.name)
            )
# TAG
class TagAdmin(CommonAdmin):
    list_editable = ['name']

#USER in general
class UserAdmin(CommonAdmin):
    list_display = ['pk', 'username', 'email', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    list_filter = ['is_staff', 'is_active']
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['-date_joined']

# USER KHONG PHAI ADMIN
class CustomerAdmin(CommonAdmin):
    list_display = ['pk', 'username', 'avatar_customer', 'email', 'address', 'is_active']
    search_fields = ['username', 'email']
    list_filter = ['is_active']
    readonly_fields = ['avatar_customer']

    def avatar_customer(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="50" height="50" style="border-radius: 50%;" />')
        return "No Avatar"


class ShopAdmin(CommonAdmin):
    list_editable = ['shop_name']
    list_display = ['pk', 'shop_name', 'shop_picture', 'owner', 'shop_address', 'active', 'created_date', 'updated_date']
    search_fields = ['name', 'description']
    list_filter = ['active', 'created_date']
    # no image show in admin, we'll worry abt this later
    readonly_fields = ['shop_picture']
    def shop_picture(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="50" height="50" style="border-radius: 50%;" />')
        return "No Avatar"

class ProductReviewAdmin(CommonAdmin):
    list_display = ['pk', 'user', 'product', 'rating', 'review_image_tag', 'content', 'active']
    search_fields = ['user__username', 'product__name', 'content']
    list_filter = ['rating', 'active', 'created_date']
    readonly_fields = ['review_image_tag']

    def review_image_tag(self, obj):
        if obj.review_image:
            return mark_safe(f'<img src="{obj.review_image.url}" width="100" height="100" />')
        return "No Image"

class ProductReviewAnswerAdmin(CommonAdmin):
    list_display = ['pk', 'review', 'author', 'content', 'active']
    search_fields = ['review__product__name', 'author__username', 'content']
    list_filter = ['active', 'created_date']

class ProductReviewVotingAdmin(CommonAdmin):
    list_display = ['pk', 'product_review', 'user_voting', 'active']
    search_fields = ['product_review__product__name', 'user_voting__username']
    list_filter = ['active']

class CustomerOrderAdmin(CommonAdmin):
    list_display = ['pk', 'customer', 'total_price', 'discount_amt', 'final_price', 'order_status', 'shipping_address', 'created_date', 'updated_date']
    search_fields = ['customer__username', 'order_status']
    list_filter = ['order_status', 'created_date', 'updated_date']
    readonly_fields = ['final_price']

class OrderItemAdmin(CommonAdmin):
    list_display = ['pk', 'order', 'product', 'quantity', 'price']
    search_fields = ['order__pk', 'product__name']
    list_filter = ['order', 'product']

class OrderDeliveryStatusAdmin(CommonAdmin):
    list_display = ['pk', 'order', 'status', 'status_message', 'created_date']
    search_fields = ['order__pk', 'status']
    list_filter = ['status', 'created_date']

class ShippingAddressAdmin(CommonAdmin):
    list_display = ['pk', 'customer', 'address_line1', 'city', 'state']
    search_fields = ['customer__username', 'address_line1', 'city', 'state']
    list_filter = ['city']

class PaymentAdmin(CommonAdmin):
    list_display = ['pk', 'order', 'payment_method', 'payment_status', 'transaction_id', 'paid_at']
    search_fields = ['order__pk', 'payment_method', 'transaction_id']
    list_filter = ['payment_status', 'payment_method']
    readonly_fields = ['transaction_id', 'paid_at']

class GroupBuyAdmin(CommonAdmin):
    list_display = ['pk', 'product', 'min_participant', 'max_participant', 'current_participant', 'price_per_person', 'start_date', 'end_date', 'is_active']
    search_fields = ['product__name']
    list_filter = ['is_active', 'start_date', 'end_date']
    readonly_fields = ['current_participant']

class GroupBuyMemberAdmin(CommonAdmin):
    list_display = ['pk', 'group_buy', 'participant', 'joined_date']
    search_fields = ['group_buy__product__name', 'participant__username']
    list_filter = ['group_buy', 'joined_date']

class CartAdmin(CommonAdmin):
    list_display = ['pk', 'customer', 'created_at']
    search_fields = ['customer__username']
    list_filter = ['created_at']

class CartItemAdmin(CommonAdmin):
    list_display = ['pk', 'cart', 'product', 'quantity']
    search_fields = ['cart__customer__username', 'product__name']
    list_filter = ['cart', 'product']

class WishlistAdmin(CommonAdmin):
    list_display = ['pk', 'customer', 'product_count']
    search_fields = ['customer__username']
    list_filter = ['customer']

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Number of Products'

class CouponAdmin(CommonAdmin):
    list_display = ['pk', 'code', 'discount_percentage', 'valid_from', 'valid_to', 'active']
    search_fields = ['code']
    list_filter = ['active', 'valid_from', 'valid_to']

class PostAdmin(CommonAdmin):
    list_display = ['pk', 'author', 'content_short', 'image_tag', 'active', 'created_date', 'updated_date']
    search_fields = ['author__username', 'content']
    list_filter = ['active', 'created_date', 'updated_date']
    readonly_fields = ['image_tag']

    def content_short(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_short.short_description = 'Content'

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "No Image"

class CommentAdmin(CommonAdmin):
    list_display = ['pk', 'post', 'author', 'content_short', 'active', 'created_date', 'updated_date']
    search_fields = ['post__product__name', 'author__username', 'content']
    list_filter = ['active', 'created_date', 'updated_date']

    def content_short(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

class PostLikeAdmin(CommonAdmin):
    list_display = ['pk', 'post', 'user', 'liked_at']
    search_fields = ['post__author__username', 'user__username']
    list_filter = ['liked_at']
#call admin.site = groupbuying site
#admin.site = GroupBuyingAdminSite()

# Register your models here.
admin_site.register(User, UserAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Product, ProductAdmin)
admin_site.register(Tag, TagAdmin)
admin_site.register(Customer, CustomerAdmin)
admin_site.register(Shop, ShopAdmin)
admin_site.register(ProductReview, ProductReviewAdmin)
admin_site.register(ProductReviewAnswer, ProductReviewAnswerAdmin)
admin_site.register(ProductReviewVoting, ProductReviewVotingAdmin)
admin_site.register(CustomerOrder, CustomerOrderAdmin)
admin_site.register(OrderItem, OrderItemAdmin)
admin_site.register(OrderDeliveryStatus, OrderDeliveryStatusAdmin)
admin_site.register(ShippingAddress, ShippingAddressAdmin)
admin_site.register(Payment, PaymentAdmin)
admin_site.register(GroupBuy, GroupBuyAdmin)
admin_site.register(GroupBuyMember, GroupBuyMemberAdmin)
admin_site.register(Cart, CartAdmin)
admin_site.register(CartItem, CartItemAdmin)
admin_site.register(Wishlist, WishlistAdmin)
admin_site.register(Coupon, CouponAdmin)
admin_site.register(Post, PostAdmin)
admin_site.register(Comment, CommentAdmin)
admin_site.register(PostLike, PostLikeAdmin)
