from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#URLS de la aplicacion
urlpatterns = [
    path('', views.HomeView, name = 'home'),
    path('login/', views.LoginView, name = 'login'),
    path('logout/', views.LogoutView, name = 'logout'),
    path('registro/', views.RegistroView, name = 'register'),
    
#URLS de la aplicacion de restaurar password
    path('reset_password/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'registro/reset_password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registro/reset_password/password_reset_confirm.html'), name='password_reset_confirm'), 
    path('reset/password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registro/reset_password/password_reset_complete.html'), name='password_reset_complete'),
]