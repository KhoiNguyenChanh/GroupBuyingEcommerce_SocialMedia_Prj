from rest_framework import viewsets, generics, parsers
from ungdunggb import serializers, paginators
from .models import Category, Product, User

# Create your views here.
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = paginators.CategoryPaginator

#product/product_id/comments
#retrieve thi no cho /{id}, list ko co
class ProductViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Product.objects.filter(active=True).all()
    serializer_class = serializers.ProductSerializer
    pagination_class = paginators.ProductPaginator

    def get_queryset(self):
        queries = self.queryset

        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(name__icontains=q)

        return queries





#createApiView -> post
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializers.UserSerialzier
    #nho cai multipart no up thang len cloudinary luon
    parser_classes = [parsers.MultiPartParser]

    # def get_permissions(self):
    #     if self.action.__eq__('current_user'):
    #         return [permissions.IsAuthenticated()]
    #
    #     return [permissions.AllowAny()]
    #
    # @action(methods=['get'], url_path='current-user' ,url_name='current-user', detail=False)
    # def current_user(self, request):
    #     return Response(serializers.UserSerialzier(request.user).data)


