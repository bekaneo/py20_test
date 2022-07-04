from django.urls import path
from products.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductViewSet)


urlpatterns = []

urlpatterns += router.urls