import django_filters
from .models import Product



class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name', 'sous_category', 'cheveux', 'tag', 'new', 'sous_category__category', 'price', 'gamme']

