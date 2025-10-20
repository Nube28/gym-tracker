from rest_framework import routers
from .api import CustomUserViewSet

router = routers.DefaultRouter()

router.register('api/v1/users', CustomUserViewSet, 'users')

urlpatterns = router.urls