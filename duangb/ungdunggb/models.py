from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now=True,null=True)
    active = models.BooleanField(default=True)
    #dùng chung nhưng ko tạo instance nào hết => trừu tượng meta
    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField()
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField(max_length=50)
    description = models.TextField()
    #1. o day tao duong dan 2.sang setting gan media root duong dan vao
    image = models.ImageField(upload_to='ungdunggb/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #them tag cho product
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.name
    #Trong th co thu foreign key den, de ko trung ten va ko trung loai foreign key
    #category = models.ForeignKey(Category, on_delete=models.CASCADE -> RESTRICT)
    # class Meta:
    #     unique_together = ('name', 'category')
    # cai con lai neu fk toi product thi unique_together = ('name', 'product')

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name