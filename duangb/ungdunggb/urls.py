from django.urls import path, include
from rest_framework import routers
from ungdunggb import views
router = routers.DefaultRouter()
#dang ki cac api
# router.register('categories', views.CategoryViewSet, basename='categories')
# router.register('products', views.ProductViewSet, basename='products')
# router.register('users', views.UserViewSet, basename='users')
# router.register('comments', views.CommentViewSet, basename='comments')
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'customers', views.CustomerViewSet, basename='customers')
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'tags', views.TagViewSet, basename='tags')
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'product-reviews', views.ProductReviewViewSet, basename='product-reviews')
router.register(r'customer-orders', views.CustomerOrderViewSet, basename='customer-orders')
router.register(r'order-items',views.OrderItemViewSet, basename='order-items')
router.register(r'shipping-addresses', views.ShippingAddressViewSet, basename='shipping-addresses')
router.register(r'coupons', views.CouponViewSet, basename='coupons')
router.register(r'group-buys',views.GroupBuyViewSet, basename='group-buys')
router.register(r'group-buy-members', views.GroupBuyMemberViewSet, basename='group-buy-members')
router.register(r'carts', views.CartViewSet, basename='carts')
router.register(r'cart-items', views.CartItemViewSet, basename='cart-items')
router.register(r'wishlists', views.WishlistViewSet, basename='wishlists')
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'comments', views.CommentViewSet, basename='comments')
router.register(r'post-likes', views.PostLikeViewSet, basename='post-likes')
router.register(r'payments', views.PaymentViewSet, basename='payments')
router.register(r'shops', views.ShopViewSet, basename='shops')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]