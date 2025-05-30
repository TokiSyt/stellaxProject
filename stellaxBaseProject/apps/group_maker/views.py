from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class GroupMaker(LoginRequiredMixin, TemplateView):
    template_name = "group_maker/group_maker.html"
    
class ListCreation(LoginRequiredMixin, TemplateView):
    template_name = "group_maker/list_creation.html"