from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),
    path("base/",views.base, name="base"),
    path('login/', views.login_view, name='login'),  # Usa la vista personalizada
    path('registro/', views.registro, name='registro'),
    path('logout/', auth_views.LogoutView.as_view(next_page='base'), name='logout'),
]