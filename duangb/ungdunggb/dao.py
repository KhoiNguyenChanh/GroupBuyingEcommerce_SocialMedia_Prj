from .models import Category, Product
from django.db.models import Count

def load_products(params={}):
    q = Product.objects.filter(active=True)

    kw = params.get('kw')
    if kw:
        q = q.filter(subject__icontains=kw)

    cate_id = params.get('cate_id')
    if cate_id:
        q = q.filter(category_id=cate_id)

    return q

def count_products_by_cate():
    return Category.objects.annotate(count=Count('product__id')).values("id", "name", "count").order_by('-count')
#r minh co the count gi nua ko :1?