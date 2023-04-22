from django.db.models import Q, Count
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination

from users.models import User
from users.serializer.user import SerializerUser, SerializerCreateUser, SerializerUpdateUser, SerializerListUser


class UserPagination(PageNumberPagination):
    page_size = 4


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SerializerUser


class UserListView(ListAPIView):
    queryset = User.objects.annotate(total_ad=Count("ad", filter=Q(ad__is_published=True))).order_by("username")
    serializer_class = SerializerListUser
    pagination_class = UserPagination


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SerializerCreateUser


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = SerializerUpdateUser


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = SerializerUser
