from django.urls import path
from .views import GroupMakerHome, GroupMakerListCreate

urlpatterns = [
    path("", GroupMakerHome.as_view(), name="home"),
    path("list-creation/", GroupMakerListCreate.as_view(), name="list-creation"),
]