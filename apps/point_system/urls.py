from django.urls import path
from .views import HomeView, DashboardView

urlpatterns = [
    path("", HomeView.as_view(), name="karma-home"),
    path("karma_dashboard/<int:pk>", DashboardView.as_view(), name="karma-dashboard"),
]
