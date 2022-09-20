from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'publications', PublicationsViewSet, basename='publication')

# URLS de la api
urlpatterns = router.urls;