from .models import (
    User, Customer, Shop, Category, Product, Tag, ProductReview,
    ProductReviewAnswer, ProductReviewVoting, CustomerOrder, OrderItem,
    OrderDeliveryStatus, ShippingAddress, Payment, GroupBuy, GroupBuyMember,
    Cart, CartItem, Wishlist, Coupon, Post, Comment, PostLike
)
from rest_framework import serializers

# Category n Tags area
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

# User Models Area
# QUAN LY NGUOI DUNG
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'avatar']
        #khong hien pass
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    #giau password khi post len
    def create(self, validated_data):
        data = validated_data.copy()

        user = User(**data) # equal user = User(first_name=data.first_name)
        user.set_password(data['password'])
        user.save()

        return user

# SERIALIZER CHO CUSTOMER
class CustomerSerializer(UserSerializer):
    address = serializers.CharField(required=False, allow_blank=True)

    class Meta(UserSerializer.Meta):
        model = Customer
        fields = UserSerializer.Meta.fields + ['address']

# SERIALIZER CHO SHOP
class ShopSerializer(serializers.ModelSerializer):
    owner = CustomerSerializer(read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'owner', 'shop_name', 'shop_address', 'shop_picture', 'shop_description', 'created_date', 'updated_date', 'active']


# Product Models Area
class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    tags = TagSerializer(many=True)

    def get_image(self, product):
        if product.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri('/static/%s' % product.image.name)
            return '/static/%s' % product.image.name
# QUAN LY PRODUCT
class ProductSerializer(BaseSerializer):
    class Meta:
        model = Product
        # fields = ['id', 'name', 'max_price', 'discount_price', 'description', 'image', 'tags', 'created_date', 'updated_date', 'category']
        fields = '__all__'

# QUAN LY COMMENT REVIEW
class ProductReviewSerializer(serializers.ModelSerializer):
    user = CustomerSerializer(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductReview
        fields = ['id', 'review_image', 'rating', 'content', 'product', 'user', 'created_date', 'updated_date', 'active']

    def validate_rating(self, value):
        if not (0 <= value <= 5):
            raise serializers.ValidationError("Rating phải nằm trong khoảng từ 0 đến 5.")
        return value

# QUAN LY TRA LOI COMMENT REVIEW
class ProductReviewAnswerSerializer(serializers.ModelSerializer):
    author = CustomerSerializer(read_only=True)
    review = serializers.PrimaryKeyRelatedField(queryset=ProductReview.objects.all())

    class Meta:
        model = ProductReviewAnswer
        fields = ['id', 'review', 'author', 'content', 'created_date', 'updated_date', 'active']

# QUAN LY VOTE BAO NHIEU SAO CHO COMMENT REVIEW
class ProductReviewVotingSerializer(serializers.ModelSerializer):
    product_review = serializers.PrimaryKeyRelatedField(queryset=ProductReview.objects.all())
    user_voting = CustomerSerializer(read_only=True)

    class Meta:
        model = ProductReviewVoting
        fields = ['id', 'product_review', 'user_voting', 'created_date', 'updated_date', 'active']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=ProductReviewVoting.objects.all(),
                fields=['product_review', 'user_voting'],
                message="Bạn đã bình chọn cho đánh giá này."
            )
        ]


# Order Models Area
# QUAN LY DIA CHI GIAO HANG
class ShippingAddressSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = ShippingAddress
        fields = ['id', 'customer', 'address_line1', 'address_line2', 'city', 'state', 'country', 'created_date', 'updated_date', 'active']

# QUAN LY SAN PHAM TRONG DON HANG
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_id', 'quantity', 'price', 'created_date', 'updated_date', 'active']

# QUAN LY DON HANG CUA KHACH
class CustomerOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    coupon = serializers.PrimaryKeyRelatedField(queryset=Coupon.objects.all(), allow_null=True, required=False)
    shipping_address = ShippingAddressSerializer(read_only=True)
    shipping_address_id = serializers.PrimaryKeyRelatedField(queryset=ShippingAddress.objects.all(), source='shipping_address', write_only=True, allow_null=True, required=False)

    class Meta:
        model = CustomerOrder
        fields = [
            'id', 'customer', 'coupon', 'total_price', 'discount_amt', 'final_price',
            'order_status', 'shipping_address', 'shipping_address_id',
            'items', 'created_date', 'updated_date', 'active'
        ]

    def create(self, validated_data):
        # XU LY TAO DON HANG VOI MA GIAM GIA (NEU CO)
        coupon = validated_data.pop('coupon', None)
        shipping_address = validated_data.pop('shipping_address', None)
        order = CustomerOrder.objects.create(**validated_data)

        if coupon:
            order.coupon = coupon
            order.discount_amt = (coupon.discount_percentage / 100) * order.total_price
            order.final_price = order.total_price - order.discount_amt
            order.save()

        if shipping_address:
            order.shipping_address = shipping_address
            order.save()

        return order
# QUAN LY THEO DOI TRANG THAI GIAO HANG
class OrderDeliveryStatusSerializer(serializers.ModelSerializer):
    order = CustomerOrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=CustomerOrder.objects.all(), source='order', write_only=True)

    class Meta:
        model = OrderDeliveryStatus
        fields = ['id', 'order', 'order_id', 'status', 'status_message', 'created_date', 'updated_date', 'active']

# QUAN LY THONG TIN THANH TOAN DON HANG
class PaymentSerializer(serializers.ModelSerializer):
    order = CustomerOrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=CustomerOrder.objects.all(), source='order', write_only=True)

    class Meta:
        model = Payment
        fields = [
            'id', 'order', 'order_id', 'payment_method', 'payment_status',
            'transaction_id', 'paid_at', 'created_date', 'updated_date', 'active'
        ]

    def validate_transaction_id(self, value):
        if Payment.objects.filter(transaction_id=value).exists():
            raise serializers.ValidationError("transaction_id đã tồn tại.")
        return value

# GroupBuy Models Area
# QUAN LY NHOM MUA CHUNG
class GroupBuySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)
    coupons = serializers.PrimaryKeyRelatedField(many=True, queryset=Coupon.objects.all(), required=False)

    class Meta:
        model = GroupBuy
        fields = [
            'id', 'product', 'product_id', 'min_participant', 'max_participant',
            'current_participant', 'price_per_person', 'start_date', 'end_date',
            'is_active', 'coupons', 'created_date', 'updated_date', 'active'
        ]

    def validate(self, data):
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("end_date phải sau start_date.")
        if data['min_participant'] > data['max_participant']:
            raise serializers.ValidationError("min_participant không thể lớn hơn max_participant.")
        return data
# QUAN LY THANH VIEN MUA CHUNG
class GroupBuyMemberSerializer(serializers.ModelSerializer):
    group_buy = GroupBuySerializer(read_only=True)
    group_buy_id = serializers.PrimaryKeyRelatedField(queryset=GroupBuy.objects.all(), source='group_buy', write_only=True)
    participant = CustomerSerializer(read_only=True)
    participant_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='participant', write_only=True)

    class Meta:
        model = GroupBuyMember
        fields = ['id', 'group_buy', 'group_buy_id', 'participant', 'participant_id', 'joined_date', 'created_date', 'updated_date', 'active']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=GroupBuyMember.objects.all(),
                fields=['group_buy', 'participant'],
                message="Người dùng đã tham gia nhóm mua này."
            )
        ]


# Cart Models Area
# QUAN LY SAN PHAM TRONG GIO HANG
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'product_id', 'quantity', 'created_date', 'updated_date', 'active']
# QUAN LY GIO HANG
class CartSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'items', 'created_at', 'updated_date', 'active']


# Wishlist Models Area
# QUAN LY DANH SACH SAN PHAM YEU THICH CUA KHACH HANG
class WishlistSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, write_only=True, required=False, source='products')

    class Meta:
        model = Wishlist
        fields = ['id', 'customer', 'products', 'product_ids', 'created_date', 'updated_date', 'active']


# Coupon Models Area
# QUAN LY MA GIAM GIA
from django.utils import timezone

class CouponSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all(), required=False)
    group_buys = serializers.PrimaryKeyRelatedField(many=True, queryset=GroupBuy.objects.all(), required=False)
    customers = serializers.PrimaryKeyRelatedField(many=True, queryset=Customer.objects.all(), required=False)

    class Meta:
        model = Coupon
        fields = [
            'id', 'code', 'discount_percentage', 'valid_from', 'valid_to',
            'active', 'coupon_type', 'products', 'group_buys', 'customers',
            'created_date', 'updated_date'
        ]

    def validate_discount_percentage(self, value):
        if not (0 < value <= 100):
            raise serializers.ValidationError("Phần trăm giảm giá phải từ 0 < discount_percentage <= 100.")
        return value

    def validate(self, data):
        if data['valid_to'] <= data['valid_from']:
            raise serializers.ValidationError("valid_to phải sau valid_from.")
        return data

 #  ƯTF ;1??
# def create(self, validated_data):
 #        products = validated_data.pop('products', [])
 #        group_buys = validated_data.pop('group_buys', [])
 #        customers = validated_data.pop('customers', [])
 #        coupon = Coupon.objects.create(**validated_data)
 #        coupon.products.set(products)
 #        coupon.group_buys.set(group_buys)
 #        coupon.customers.set(customers)
 #        return coupon
 #
 #    def update(self, instance, validated_data):
 #        products = validated_data.pop('products', None)
 #        group_buys = validated_data.pop('group_buys', None)
 #        customers = validated_data.pop('customers', None)
 #
 #        for attr, value in validated_data.items():
 #            setattr(instance, attr, value)
 #
 #        if products is not None:
 #            instance.products.set(products)
 #        if group_buys is not None:
 #            instance.group_buys.set(group_buys)
 #        if customers is not None:
 #            instance.customers.set(customers)
 #
 #        instance.save()
 #        return instance


# Social Media Models Area
# QUAN LY LUOT THICH BAI VIET (TBH, STILL DONT LIKE THE 'POST_LIKE' NAME)
class PostLikeSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    user = CustomerSerializer(read_only=True)

    class Meta:
        model = PostLike
        fields = ['id', 'post', 'user', 'liked_at', 'created_date', 'updated_date', 'active']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=PostLike.objects.all(),
                fields=['post', 'user'],
                message="Bạn đã thích bài viết này."
            )
        ]
# QUAN LY CAC BAI VIET CUA NGUOI DUNG
class PostSerializer(serializers.ModelSerializer):
    author = CustomerSerializer(read_only=True)
    likes = PostLikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'likes', 'created_date', 'updated_date', 'active']

# QUAN LY COMMENT BAI VIET
class CommentSerializer(serializers.ModelSerializer):
    author = CustomerSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='post', write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'post_id', 'author', 'content', 'created_date', 'updated_date', 'active']


# b. Phương Thức pop Là Gì?
# Trong Python, pop là một phương thức của các đối tượng từ điển (dict) dùng để:
#
# Loại bỏ một cặp khóa-giá trị khỏi từ điển.
# Trả về giá trị của khóa vừa bị loại bỏ.
# Cú pháp chung của pop:
#

# value = dictionary.pop('key', default_value)
# 'key': Khóa mà bạn muốn loại bỏ khỏi từ điển.
# default_value (tuỳ chọn): Giá trị mặc định trả về nếu khóa không tồn tại trong từ điển.

# Tại Sao Sử Dụng validated_data.pop Trong Serializers?
# Trong các phương thức như create hoặc update của serializers, bạn thường cần xử lý các trường dữ liệu một cách đặc biệt trước khi tạo hoặc cập nhật các đối tượng model. Một số lý do bao gồm:
#
# Xử lý các trường dữ liệu không trực tiếp liên kết với model: Ví dụ, xác nhận mật khẩu (password2) trong quá trình đăng ký người dùng.
# Tách biệt dữ liệu để tạo các đối tượng liên quan: Ví dụ, tạo một đối tượng Customer sau khi tạo đối tượng User.
# Sử dụng pop giúp bạn:
#
# Loại bỏ các trường dữ liệu không cần thiết khỏi validated_data để tránh lỗi khi tạo đối tượng model.
# Trích xuất các giá trị từ validated_data để xử lý chúng theo cách riêng biệt.