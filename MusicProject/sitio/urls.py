from django.urls import path
from . import views

#URLS de la aplicacion
urlpatterns = [
    path('', views.HomeView, name = 'home'), 
    path('profile/', views.UserProfile, name = 'profile')
]