from rest_framework import routers
from .api import ExcerciseDoneViewSet

router = routers.DefaultRouter()

routers.register('api/v1/excercise-done', ExcerciseDoneViewSet, 'excercise-done')

urlpatterns = router.urls