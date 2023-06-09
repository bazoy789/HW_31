from rest_framework import serializers

from users.models import Location


class LocationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"