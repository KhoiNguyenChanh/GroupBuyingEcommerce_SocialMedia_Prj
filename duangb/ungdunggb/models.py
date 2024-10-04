from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    # dùng chung nhưng ko tạo instance nào hết => trừu tượng meta
    class Meta:
        abstract = True


# USER MODELS AREA
class User(AbstractUser, BaseModel):
    avatar = CloudinaryField('avatar', null=True)
    address = models.TextField(null=True, blank=True)


class Customer(User):

    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.username


# MỌI USER LẦN ĐẦU ĐKY ĐỀU LÀ CUSTOMER, CÁC CUSTOMER CÓ QUYỀN ĐƯỢC TRỞ THÀNH 1 SELLER BẰNG CÁCH TẠO SHOP
class Shop(BaseModel):
    owner = models.OneToOneField(Customer, on_delete=models.CASCADE)  # Link to the Customer
    shop_name = models.CharField(max_length=255)
    shop_address = models.TextField(null=True, blank=True)
    shop_picture = CloudinaryField('shop_picture', null=True, blank=True)
    shop_description = models.TextField(null=True, blank=True)

    # unique_together là không cần thiết: OneToOneField đã đảm bảo tính duy nhất, do đó unique_together với một trường là không cần thiết và có thể gây nhầm lẫn.
    # class Meta:
    #     unique_together = ('owner',)  # Ensure a customer can only have one shop

    def __str__(self):
        return self.shop_name


# CATEGORY AND PRODUCT AREA
class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)

    # max_price = models.CharField(max_length=255)
    # discount_price = models.CharField(max_length=255)
    max_price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    # discount alwways < max, will add in restrain later hehe
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    in_stock_total = models.PositiveIntegerField(default=1)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    added_by_user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='added_products', null=True)
    # them tag cho product
    tags = models.ManyToManyField('Tag', related_name='products')

    image = models.ImageField(upload_to='ungdunggb/%Y/%m', null=True)

    # to prevent unforseen problems, i suggest you use ImageField insted
    # image = CloudinaryField('image', null = True)
    def __str__(self):
        return self.name
    # 1. o day tao duong dan 2.sang setting gan media root duong dan vao
    # image = models.ImageField(upload_to='ungdunggb/%Y/%m')

    # Trong th co thu foreign key den, de ko trung ten va ko trung loai foreign key
    # category = models.ForeignKey(Category, on_delete=models.CASCADE -> RESTRICT)
    # class Meta:
    #     unique_together = ('name', 'category')
    # cai con lai neu fk toi product thi unique_together = ('name', 'product')


# class ProductImage(BaseModel):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
#     product_image = CloudinaryField('product_image', null=True)
#
#     def __str__(self):
#         return f"Image for {self.product.name}"

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ProductReview(BaseModel):
    review_image = models.ImageField(upload_to='ungdunggb/%Y/%m', null=True)
    rating = models.IntegerField(default=5)
    content = models.TextField(default='')
    # answer = models.CharField(max_length=255, null=False)
    # ->ProductReviewComment
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"


class ProductReviewAnswer(BaseModel):
    review = models.ForeignKey(ProductReview, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='review_answers')
    content = models.TextField()

    def __str__(self):
        return f"Answer to Review {self.review.id}"
# f"...": Đây là một chuỗi định dạng (f-string),
# cho phép bạn nhúng các biểu thức Python vào trong chuỗi.
# Bất kỳ biến nào nằm trong dấu ngoặc nhọn {}
# sẽ được thay thế bằng giá trị của nó.

class ProductReviewVoting(BaseModel):
    product_review = models.ForeignKey(ProductReview, on_delete=models.CASCADE, related_name='votings')
    user_voting = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='review_votings')

    class Meta:
        unique_together = ('product_review', 'user_voting')

    def __str__(self):
        return f"{self.user_voting.username} voted on Review {self.product_review.id}"


class CustomerOrder(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50,
                                    default='Pending')  # Ví dụ: Pending, Processing, Completed, Cancelled
    shipping_address = models.ForeignKey('ShippingAddress', on_delete=models.SET_NULL, null=True, blank=True)

    # payment = models.OneToOneField('Payment', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"
    # # product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    # purchase_price = models.CharField(max_length=255)
    # coupon_code = models.CharField(max_length=255)
    # # d_amt: reduced in price or tax amount
    # discount_amt = models.CharField(max_length=255)
    # product_status = models.CharField(max_length=255)


# SPHAM TRONG DON HANG
class OrderItem(BaseModel):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"


class OrderDeliveryStatus(BaseModel):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='delivery_statuses')
    status = models.CharField(max_length=255)
    status_message = models.CharField(max_length=255)

    def __str__(self):
        return f"Status for Order {self.order.id}: {self.status}"


# SHIPPING INFO
class ShippingAddress(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shipping_addresses')
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    # postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"Shipping Address for {self.customer.username}"


# PAYMENT METHOD
class Payment(BaseModel):
    order = models.OneToOneField(CustomerOrder, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50, default='Pending')
    transaction_id = models.CharField(max_length=100, unique=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Payment for Order {self.order.id}"


# mo hinh mua chung
class GroupBuy(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='group_buys')
    min_participant = models.PositiveIntegerField(default=2)  # Số lượng người cần để thành công
    max_participant = models.PositiveIntegerField(default=10)
    current_participant = models.PositiveIntegerField(default=1)  # Số lượng hiện tại
    # gia moi nguoi trong nhóm
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    # thoi gian bat dau va ket thuc nhom mua
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # QUAN LY, CO THE SOFT LOCK CAI GROUP NAY LAI
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"GroupBuy for {self.product.name} by {self.product.added_by_user.username}"


class GroupBuyMember(BaseModel):
    group_buy = models.ForeignKey(GroupBuy, on_delete=models.CASCADE, related_name='members')
    participant = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='group_buy_participations')
    # ngay tham gia nhom
    joined_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('group_buy', 'participant')

    def __str__(self):
        return f"{self.participant.username} joined {self.group_buy}"


class Cart(BaseModel):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.customer.username}"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.cart.customer.username}'s cart"


# Loved product
class Wishlist(BaseModel):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product, related_name='wishlisted_by')

    def __str__(self):
        return f"Wishlist of {self.customer.username}"


class Coupon(BaseModel):
    COUPON_TYPE_CHOICES = [
        ('individual', 'Cá nhân'),
        ('group', 'Nhóm'),
    ]

    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    coupon_type = models.CharField(max_length=10, choices=COUPON_TYPE_CHOICES, default='individual')

    # Liên kết đến sản phẩm
    products = models.ManyToManyField('Product', related_name='coupons', blank=True)

    # Liên kết đến nhóm mua
    group_buys = models.ManyToManyField('GroupBuy', related_name='coupons', blank=True)
    # Liên kết đến khách hàng
    customers = models.ManyToManyField('Customer', related_name='coupons', blank=True)

    def __str__(self):
        return f"Coupon {self.code} - {self.coupon_type}"
    # code = models.CharField(max_length=50, unique=True)
    # discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    # # XU LY VALID_TO PHAI > VALID_FROM, LATER HEHE
    # valid_from = models.DateTimeField()
    # valid_to = models.DateTimeField()
    # active = models.BooleanField(default=True)
    #
    # def __str__(self):
    #     return f"Coupon {self.code}"


# SOCIAL MEDIA'S MODEL AREA

class Post(BaseModel):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='posts')
    content = RichTextField()
    image = CloudinaryField('post_image', null=True, blank=True)
    likes = models.ManyToManyField(Customer, through='PostLike', related_name='liked_posts')

    def __str__(self):
        return f"Post by {self.author.username}"


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',null=True)
    author = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='post_comments',  null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.id}"


class PostLike(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='post_likes_posts')
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} likes Post {self.post.id}"

# class Interaction(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
#     # comment, review tren spham nao
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
#
#     class Meta:
#         abstract = True
#
# # danh gia san pham, rating review o tren la danh gia comment
# class Rating(Interaction):
#     rate = models.SmallIntegerField(default=0)
#
# class Comment(Interaction):
#     content = models.CharField(max_length=255, null=False)
#
#
# # like comment san pham ? chi like 1 lan (nhu facebook, nho unique together)
# class Like(Interaction):
#     active = models.BooleanField(default=True)
#
#     class Meta:
#         unique_together = ('user', 'product')
#
#
# # rating 0-5
