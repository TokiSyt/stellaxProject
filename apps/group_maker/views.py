from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GroupCreationForm
from .models import GroupCreationModel
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme

class GroupHome(LoginRequiredMixin, TemplateView):
    template_name = "group_maker/home.html"
    form_class = GroupCreationModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = GroupCreationModel.objects.filter(user=self.request.user)
        context["form"] = self.form_class()
        return context

class GroupCreate(LoginRequiredMixin, CreateView):
    model = GroupCreationModel
    template_name = "group_maker/list_create.html"
    form_class = GroupCreationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.POST.get("next") or self.request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return "/"


class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = GroupCreationModel
    template_name = "group_maker/list_edit.html"
    form_class = GroupCreationForm

    def get_success_url(self):
        next_url = self.request.POST.get("next") or self.request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected_group"] = self.object
        return context


class GroupDelete(LoginRequiredMixin, DeleteView):
    model = GroupCreationModel
    template_name = "group_maker/confirm_delete.html"

    def get_success_url(self):
        next_url = self.request.POST.get("next") or self.request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected_group"] = self.object
        return context
