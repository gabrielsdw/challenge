from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrReadOnly
from .serializers import UserModelSerializer, UserDetailModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics

User = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserModelSerializer
    permission_classes = []


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
