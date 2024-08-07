from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from tuto.quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.order_by("-name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
