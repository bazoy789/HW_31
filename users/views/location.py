from rest_framework.viewsets import ModelViewSet

from users.models import Location
from users.serializer.location import LocationSerializers


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers
