from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # defines the project's root url
    path('', views.index, name='home'), 
    # <> brackets "capture" part of a URL to send it as an argument to a view method
    path('view_card?<str:operation>', views.viewCard, name='view_card'), 
]