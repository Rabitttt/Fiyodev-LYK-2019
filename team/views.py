from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView
from users.forms import TeamCreateForm
from .models import Team


class ListTeam(ListView):
    template_name = "team_list.html"
    queryset = Team.objects.all()
    context_object_name = 'teamlist'


class TeamCreate():
    model = Team
    form_class = TeamCreateForm
