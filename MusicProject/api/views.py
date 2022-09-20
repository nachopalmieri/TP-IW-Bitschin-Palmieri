from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from tuneup.models.publications import MusicHit, PUB_STATE_ACTIVE

from .serializers import *


class PublicationsViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        
        queryset = MusicHit.objects.all(state=PUB_STATE_ACTIVE)
        pub = get_object_or_404(queryset, pk=pk)
        serializer = MusicHitSerializer(pub)
        
        return Response(serializer.data)