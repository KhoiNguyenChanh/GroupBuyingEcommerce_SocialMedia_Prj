from .models import Category, Product, Tag, User
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    tags = TagSerializer(many=True)

    def get_image(self, product):
        if product.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri('/static/%s' % product.image.name)
            return '/static/%s' % product.image.name

class ProductSerializer(BaseSerializer):

    class Meta:
        model = Product
        fields = '__all__'



class UserSerialzier(serializers.ModelSerializer):
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
#tao cac loai user rieng biet nhu seller, customer
