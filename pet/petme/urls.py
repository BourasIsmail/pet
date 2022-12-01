from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name="index"), 
    path('login_sign/', views.login_sign, name="login_sign"),
    path('ChoixPet/', views.ChoixPet, name="ChoixPet"),
    path('donate/', views.donate, name="donate"),
    path('profil/', views.profil, name="profil"),
    ]