from rest_framework import viewsets

from consumer.models import ApiUser
from consumer.serializers import ApiUserSerializer


# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'path', 'get']
    serializer_class = ApiUserSerializer

