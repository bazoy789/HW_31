from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from app.models import Ad, Selection
from app.serializer import SerializerAd, SerializerAdList, SerializerSelection, SerializerListSelection, \
    SerializerCreateSelection, SerializerDetailSelection

from app.permissions import IsOwner


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.order_by("name")
    default_serializer_class = SerializerSelection

    default_permission = [AllowAny]
    permissions = {
        "create": [IsAuthenticated],
        "update": [IsAuthenticated, IsOwner],
        "partial_update": [IsAuthenticated, IsOwner],
        "destroy": [IsAuthenticated, IsOwner],
    }

    serializer = {
        "list": SerializerListSelection,
        "create": SerializerCreateSelection,
        "retrieve": SerializerDetailSelection,
    }
    # "retrieve": SerializerAdDetail

    def get_serializer_class(self):
        return self.serializer.get(self.action, self.default_serializer_class)

    def get_permission(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]
