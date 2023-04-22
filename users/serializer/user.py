
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from users.models import User, Location
from users.serializer.location import LocationSerializers


class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


class SerializerDetailUser(serializers.ModelSerializer):
    location = LocationSerializers(many=True)

    class Meta:
        model = User
        exclude = ["password"]


class SerializerListUser(serializers.ModelSerializer):
    # Пример
    # total_ads = SerializerMethodField()
    #
    # def get_total_ads(self, user):
    #     return user.ad_set.filter(is_published=True).count()
    total_ad = serializers.IntegerField()

    class Meta:
        model = User
        exclude = ["password"]


class SerializerCreateUser(serializers.ModelSerializer):

    location = SlugRelatedField(
        required=False,
        many=True,
        slug_field='name',
        queryset=Location.objects.all(),
    )

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        # passwd = validated_data.pop("password")
        new_user = User.objects.create(**validated_data)
        # new_user.set_password(passwd)
        # new_user.save()
        for loc_name in self._location:
            loc, _ = Location.objects.get_or_create(name=loc_name)
            new_user.location.add(loc)
        return new_user

    class Meta:
        model = User
        fields = "__all__"


class SerializerUpdateUser(serializers.ModelSerializer):

    location = SlugRelatedField(
        required=False,
        many=True,
        slug_field='name',
        queryset=Location.objects.all(),
    )

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)
        user.location.clear()
        for loc_name in self._location:
            loc, _ = Location.objects.get_or_create(name=loc_name)
            user.location.add(loc)
        return user

    class Meta:
        model = User
        fields = "__all__"
