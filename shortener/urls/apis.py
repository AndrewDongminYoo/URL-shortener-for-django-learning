from django.http import Http404, JsonResponse
from rest_framework.decorators import renderer_classes, action
from rest_framework.renderers import JSONRenderer
from shortener.models import ShortenedUrls
from shortener.urls.serializers import UrlListSerializer, UrlCreateSerializer
from rest_framework import viewsets, permissions, status
from shortener.users.utils import url_count_changer


class UrlListView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShortenedUrls.objects.order_by("-created_at")
    serializer_class = UrlListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, **kwargs):
        # POST METHOD
        serializer = UrlCreateSerializer(data=request.data)
        if serializer.is_valid():
            rtn = serializer.create(request, serializer.data)
            return JsonResponse(UrlListSerializer(rtn).data, status=status.HTTP_201_CREATED)
        pass

    def retrieve(self, request, pk=None, **kwargs):
        # Detail GET
        queryset = self.get_queryset().filter(pk=pk).first()
        serializer = UrlListSerializer(queryset)
        return JsonResponse(serializer.data)

    def update(self, request, pk=None, **kwargs):
        # PUT METHOD
        pass

    def partial_update(self, request, pk=None, **kwargs):
        # PATCH METHOD
        pass

    @renderer_classes([JSONRenderer])
    def destroy(self, request, pk=None, **kwargs):
        # DELETE METHOD
        queryset = self.get_queryset().filter(pk=pk, creator_id=request.user.id)
        if not queryset.exists():
            raise Http404
        queryset.delete()
        url_count_changer(request, False)
        return JsonResponse(status=status.HTTP_200_OK, data=dict(msg="ok", id=pk))

    def list(self, request, **kwargs):
        # GET ALL
        queryset = self.get_queryset().all()
        serializer = UrlListSerializer(queryset, many=True)
        return JsonResponse(serializer.data)

    @action(detail=True, methods=["get"])
    def add_click(self, request, pk=None):
        queryset = self.get_queryset().filter(pk=pk, creator_id=request.user.id)
        if not queryset.exists():
            raise Http404
        rtn = queryset.first().clicked()
        serializer = UrlListSerializer(rtn)
        return JsonResponse(serializer.data)
