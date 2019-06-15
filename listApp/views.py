from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.parsers import FileUploadParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from listApp.models import Item
from listApp.serializers import UserSerializer, GroupSerializer, ItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    renderer_classes = (JSONRenderer,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    renderer_classes = (JSONRenderer,)


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    renderer_classes = (JSONRenderer,)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        uploadedIds = {}
        for key, val in request.data.items():
            item = Item.objects.get(id=key)
            item.photo = val
            item.save()
            uploadedIds[item.id] = "http://localhost:8000" + item.photo.url

        return Response(uploadedIds, status=status.HTTP_200_OK)
