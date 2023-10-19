# pages/urls.py

from django.urls import path
from . import views

# include(route, view, name)
urlpatterns = [
    path('', views.index, name='home'),
]