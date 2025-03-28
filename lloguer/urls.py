from django.urls import path
from . import views

urlpatterns = [
    path('autos', views.veure_autos, name='llista_autos'),
]