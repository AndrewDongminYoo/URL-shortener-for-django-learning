from shortener.models import ShortenedUrls, Users
from shortener.urls.serializers import UserSerializer, UrlListSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response


class UserView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShortenedUrls.objects.order_by("-created_at")
    serializer_class = UrlListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, **kwargs):
        # POST METHOD
        pass

    def retrieve(self, request, pk=None, **kwargs):
        # Detail GET
        queryset = self.get_queryset().filter(pk=pk)
        serializer = UrlListSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None, **kwargs):
        # PUT METHOD
        pass

    def partial_update(self, request, pk=None, **kwargs):
        # PATCH METHOD
        pass

    def destroy(self, request, pk=None, **kwargs):
        # DELETE METHOD
        pass

    def list(self, request, **kwargs):
        # GET ALL
        queryset = self.get_queryset().all()
        serializer = UrlListSerializer(queryset, many=True)
        return Response(serializer.data)