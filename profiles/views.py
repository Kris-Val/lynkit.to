from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Link, Profile
from .serializers import LinkSerializer, ProfileSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.user == request.user
            if hasattr(obj, "user")
            else obj.profile.user == request.user
        )


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # each user only sees their own profile
        return Profile.objects.filter(user=self.request.user)


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # only links belonging to the logged-in user
        return Link.objects.filter(profile__user=self.request.user)

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(profile=profile)

    @action(detail=True, methods=["post"])
    def move_up(self, request, pk=None):
        link = self.get_object()
        link.move_up()
        return Response({"status": "moved up"})

    @action(detail=True, methods=["post"])
    def move_down(self, request, pk=None):
        link = self.get_object()
        link.move_down()
        return Response({"status": "moved down"})
