from django.urls import path
from . import views

urlpatterns = [
    path('', views.me, name='about-me'),
]