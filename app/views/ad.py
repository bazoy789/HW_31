from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from app.models import Ad
from app.serializer import SerializerAd, SerializerAdList

from app.permissions import IsStuff, IsOwner


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.order_by("-price")
    default_serializer_class = SerializerAd

    default_permission = [AllowAny]
    permissions = {
        "retrieve": [IsAuthenticated],
        "update": [IsAuthenticated, IsStuff | IsOwner],
        "partial_update": [IsAuthenticated, IsStuff | IsOwner],
        "destroy": [IsAuthenticated, IsStuff | IsOwner],
    }

    serializer = {
        "list": SerializerAdList
    }
    # "retrieve": SerializerAdDetail

    def get_serializer_class(self):
        return self.serializer.get(self.action, self.default_serializer_class)

    def get_permission(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def list(self, request, *args, **kwargs):
        cat = request.GET.getlist("cat", [])
        if cat:
            self.queryset = self.queryset.filter(category_id__in=cat)

        location = request.GET.get("location", [])
        if location:
            self.queryset = self.queryset.filter(author_id__location__name__icontains=location)

        text = request.GET.get("text", [])
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        price_from = request.GET.get("price_from", [])
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        price_to = request.GET.get("price_to", [])
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)
