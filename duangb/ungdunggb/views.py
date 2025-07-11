# from crypt import methods
from rest_framework import viewsets, generics, status, parsers, permissions
from rest_framework.generics import get_object_or_404
from ungdunggb import serializers, paginators
from . import perms
from ungdunggb.models import Category, Product, User, Comment, Like, Rating
from requests import Response
from rest_framework.decorators import action
from rest_framework.response import Response



# Create your views here.
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = paginators.CategoryPaginator


#product/product_id
#retrieve thi no cho /{id}, list ko co
class ProductViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Product.objects.filter(active=True).all()
    serializer_class = serializers.ProductDetailSerializer
    # search theo id thi khoi phan trang :))
    # pagination_class = paginators.ProductPaginator

    # tim theo keyword
    def get_queryset(self):
        queries = self.queryset

        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(name__icontains=q)

        return queries

     # chung thuc cho viec add comment
    permission_classes = [permissions.AllowAny()]

    @action(methods=['post'], url_path='comments', detail=True)
    def get_permissions(self):
        if self.action in ['add_comment', 'like']:
            #  la doi tuong nen isauthenticated co ngoac va nguoc lai
            return [permissions.IsAuthenticated()]
        return self.permission_classes

    # url_path => .../../url_path, vd: /product/{producct_id}/comments/
    @action(methods=['post'], url_path='comments', detail=True)
    # co tim id product => detail = true, detail = true => def (..., pk):
    def add_comment(self, request, pk):
        # lay current_user
        c = Comment.objects.create(user=request.user, product=self.get_object(), content=request.data.get('content'))

        return Response(serializers.CommentSerializer(c).data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], url_path='like', detail=True)
    def like(self, request, pk):
        like, created = Like.objects.get_or_create(user=request.user, product=self.get_object())
        # 0 like => like, 1 like => 0 like
        if not created:
            like.active = not like.active
            like.save()

        return Response(serializers.ProductDetailSerializer(self.get_object(), context={'request': request}).data,
                        status=status.HTTP_200_OK)


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


class CommentViewSet(viewsets.ViewSet,generics.ListAPIView, generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    # permission_classes = [perms.OwnerAuthenticated]

# class CommentViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = serializers.CommentSerializer
     # permission_classes = [perms.py.OwnerAuthenticated]
# =/= /product/product-id/comment/

