from rest_framework import routers
from .api import ExcerciseViewSets

router = routers.DefaultRouter()

routers.register('api/v1/excercises', ExcerciseViewSets, 'excercises')

urlpatterns = router.urls