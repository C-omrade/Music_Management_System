from django.urls import path,include
from .views import *
urlpatterns = [
    path('songs/',SongsListView.as_view(),name='songs'),
]