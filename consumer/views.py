from rest_framework import viewsets

from consumer.models import ApiUser, Category, Warhouse, Product
from consumer.serializers import ApiUserSerializer, CategorySerializer, \
    WarhouseSerializer, ProductSerializer


# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'path', 'get']
    serializer_class = ApiUserSerializer

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def __str__(self):
        return self.name

class WarhouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warhouse.objects.all()
    serializer_class = WarhouseSerializer

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

