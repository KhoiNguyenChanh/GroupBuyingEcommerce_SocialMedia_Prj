from django.urls import path, include
from rest_framework import routers
# from ungdunggb import views
router = routers.DefaultRouter()
#dang ki cac api
# router.register('categories', views.CategoryViewSet, basename='categories')
# router.register('products', views.ProductViewSet, basename='products')
# router.register('users', views.UserViewSet, basename='users')
# router.register('comments', views.CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls)),

]