from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from tuneup.models.publications import MusicHit, PUB_STATE_ACTIVE

from .serializers import MusicHitSerializer


class PublicationPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

class PublicationsViewSet(viewsets.ModelViewSet):
    serializer_class = MusicHitSerializer
    pagination_class = PublicationPagination
    queryset = MusicHit.objects.filter(state=PUB_STATE_ACTIVE)