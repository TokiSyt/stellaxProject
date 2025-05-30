from django.urls import path
from .views import GroupMaker, ListCreation

urlpatterns = [
    path("", GroupMaker.as_view(), name="home"),
    path("list-creation/", ListCreation.as_view(), name="list-creation"),
]