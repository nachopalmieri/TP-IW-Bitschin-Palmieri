from django.urls import path, include
from . import views

#URLS de la aplicacion
urlpatterns = [
    path('', views.HomeView, name = 'home'), 
    path('accounts/', include ('allauth.urls')),
    path('profile/', views.UserProfile, name = 'profile')
]