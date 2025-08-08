from django.shortcuts import render, get_object_or_404
from .services.group_split import group_split as group_split_f
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import GroupCreationModel
from .forms import GroupCreationForm, GroupMakerForm


class GroupMakerHome(LoginRequiredMixin, TemplateView):
    template_name = "group_maker/home.html"
    form_class = GroupMakerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = GroupCreationModel.objects.all()
        context["form"] = self.form_class()
        context["group_split"] = kwargs.get("group_split")
        context["selected_group"] = kwargs.get("selected_group")
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            group_id = request.POST.get("group_id")
            group_size = form.cleaned_data["size"]

            group = GroupCreationModel.objects.get(id=group_id)
            members = group.get_members_list()

            group_split = group_split_f(members, group_size)

            return render(
                request,
                "group_maker/home.html",
                {
                    "form": form,
                    "group_split": group_split,
                    "groups": GroupCreationModel.objects.all(),
                    "selected_group": group,
                },
            )
        return render(request, "group_maker/home.html", {"form": form})


class GroupMakerListCreate(LoginRequiredMixin, CreateView):
    model = GroupCreationModel
    template_name = "group_maker/list_create.html"
    form_class = GroupCreationForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("home")
