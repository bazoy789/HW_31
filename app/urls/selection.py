
from django.urls import path, include
from rest_framework import routers

from app.views.selection import SelectionViewSet

router = routers.SimpleRouter()
router.register("", SelectionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
