""" cards/urls.py """
from django.urls import path
from . import views

urlpatterns = [
    # go to flashcards menu by default
    path('', views.menu, name='menu'), 
    # <> brackets "capture" part of a URL to send it as an argument to a view method
    path('viewCard?<str:operation>', views.viewCard, name='view_card'), 
    path('viewResult', views.viewResult, name='view_result'),
]