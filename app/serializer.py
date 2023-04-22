from rest_framework import serializers
from rest_framework.fields import BooleanField
from rest_framework.relations import SlugRelatedField

from app.models import Ad, Category, Selection
from app.validators import check_is_publish
from users.models import User
from users.serializer.user import SerializerDetailUser


class SerializerAd(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = "__all__"


class SerializerAdList(serializers.ModelSerializer):
    author_id = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category_id = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


class SerializerAdCreate(serializers.ModelSerializer):
    author_id = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category_id = SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    is_published = BooleanField(validators=[check_is_publish], required=False)

    class Meta:
        model = Ad
        fields = "__all__"


class SerializerAdDetail(serializers.ModelSerializer):
    author = SerializerDetailUser()
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


class SerializerSelection(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = "__all__"


class SerializerDetailSelection(serializers.ModelSerializer):
    items = SerializerAd(many=True)

    class Meta:
        model = Selection
        fields = "__all__"


class SerializerListSelection(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field="name", queryset=User.objects.all())

    class Meta:
        model = Selection
        fields = ["owner", "name"]


class SerializerCreateSelection(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field="name", read_only=True)

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data["owner"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = "__all__"
