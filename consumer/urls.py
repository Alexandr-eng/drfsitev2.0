from rest_framework.routers import DefaultRouter

from consumer.views import UserModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)

urlpatterns = [


]
urlpatterns.extend(router.urls)