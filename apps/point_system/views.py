from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.group_maker.models import GroupCreationModel


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "point_system/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = GroupCreationModel.objects.filter(user=self.request.user)
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "wip.html"
