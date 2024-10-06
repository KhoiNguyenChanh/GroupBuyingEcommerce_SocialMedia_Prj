# from crypt import methods
from rest_framework import viewsets, generics, status, parsers, permissions
from rest_framework.generics import get_object_or_404
from ungdunggb import serializers, paginators
from . import perms
from ungdunggb.models import (
    Category, Product, User, Comment,
    Customer, CustomerOrder, OrderItem, ShippingAddress, Coupon,
    GroupBuy, GroupBuyMember, Cart, CartItem, Post, PostLike, Payment,
    ProductReview, Wishlist, Shop
)
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # pagination_class = paginators.CategoryPaginator


#product/product_id
#retrieve thi no cho /{id}, list ko co
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(active=True).all()
    serializer_class = serializers.ProductSerializer
    # pagination_class = paginators.ProductPaginator

    # tim theo keyword
    def get_queryset(self):
        queries = self.queryset

        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(name__icontains=q)

        return queries

     # chung thuc cho viec add comment
    permission_classes = [permissions.AllowAny]

    # @action(methods=['post'], url_path='comments', detail=True)
    # def get_permissions(self):
    #     if self.action in ['add_comment', 'like']:
    #         #  la doi tuong nen isauthenticated co ngoac va nguoc lai
    #         return [permissions.IsAuthenticated()]
    #     return self.permission_classes

    # url_path => .../../url_path, vd: /product/{producct_id}/comments/
    @action(methods=['post'], url_path='reviews', detail=True)
    # co tim id product => detail = true, detail = true => def (..., pk):
    def add_review(self, request, pk):
        # lay current_user
        r = ProductReview.objects.create(user=request.customer, product=self.get_object(), content=request.data.get('content'), rating=request.data.get('rating'))
        return Response(serializers.ProductReviewSerializer(r).data, status=status.HTTP_201_CREATED)

    # @action(methods=['post'], url_path='like', detail=True)
    # def like(self, request, pk):
    #     like, created = Like.objects.get_or_create(user=request.user, product=self.get_object())
    #     # 0 like => like, 1 like => 0 like
    #     if not created:
    #         like.active = not like.active
    #         like.save()
    #
    #     return Response(serializers.ProductDetailSerializer(self.get_object(), context={'request': request}).data,
    #                     status=status.HTTP_200_OK)


#createApiView -> post
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializers.UserSerializer
    #nho cai multipart no up thang len cloudinary luon
    parser_classes = [parsers.MultiPartParser]


    def get_permissions(self):
        if self.action.__eq__('current_user'):
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    # /user/current_user (da dc chung thuc)
    #detail=false vi ko khai bao id gui len
    @action(detail=False, url_path='current-user', url_name='current-user', methods=['get'])
    def current_user(self, request):
        return Response(serializers.UserSerializer(request.user).data)

# productreview
class ProductReviewViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.DestroyAPIView, generics.CreateAPIView):
    queryset = ProductReview.objects.filter(active=True).all()
    serializer_class = serializers.ProductReviewSerializer
# shop
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = serializers.ShopSerializer
# CUSTOMER VIEWSET
class CustomerViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Customer.objects.filter(is_active=True).all()
    serializer_class = serializers.CustomerSerializer

# TAGVIEWSET
class TagViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.TagSerializer

# CUSTOMERORDERVIEWSET
class CustomerOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = serializers.CustomerOrderSerializer

# ORDER ITEM VIEWSET
class OrderItemViewSet(viewsets.ViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
# shippingaddressviewset
class ShippingAddressViewSet(viewsets.ModelViewSet):

    queryset = ShippingAddress.objects.all()
    serializer_class = serializers.ShippingAddressSerializer
# couponviewset
class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = serializers.CouponSerializer

class GroupBuyViewSet(viewsets.ModelViewSet):
    queryset = GroupBuy.objects.all()
    serializer_class = serializers.GroupBuySerializer

class GroupBuyMemberViewSet(viewsets.ModelViewSet):
    queryset = GroupBuyMember.objects.all()
    serializer_class = serializers.GroupBuyMemberSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = serializers.CartItemSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = serializers.PostLikeSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
# class CommentViewSet(viewsets.ViewSet,generics.ListAPIView, generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = serializers.CommentSerializer
#     # permission_classes = [perms.OwnerAuthenticated]

# class CommentViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = serializers.CommentSerializer
     # permission_classes = [perms.py.OwnerAuthenticated]
# =/= /product/product-id/comment/

