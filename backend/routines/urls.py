from rest_framework import routers
from .api import DayViewSet, DayExcerciseViewSet, RoutineViewSet

router = routers.DefaultRouter()

router.register('api/v1/days', DayViewSet, 'days')
router.register('api/v1/days-excercise', DayExcerciseViewSet, 'days-excercise')
router.register('api/v1/routines', RoutineViewSet, 'routines')

urlpatterns = router.urls