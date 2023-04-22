
from django.urls import path, include
from rest_framework import routers

from app.views.ad import AdViewSet

router = routers.SimpleRouter()
router.register("", AdViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
