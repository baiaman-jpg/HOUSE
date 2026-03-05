from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, ReviewViewSet

router = DefaultRouter()

router.register("properties", PropertyViewSet)
router.register("reviews", ReviewViewSet)

urlpatterns = router.urls