from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from team.forms import TeamCreateForm
from .models import Team


class ListTeam(ListView):
    template_name = "team_list.html"
    queryset = Team.objects.all()
    context_object_name = 'teamlist'



class TeamCreate(CreateView):
    form_class = TeamCreateForm
    model = Team
    success_url = reverse_lazy("teamlist")
    template_name = "team/create_team.html"

    def form_valid(self, form):

        form.instance.owner=self.request.user
        return super(TeamCreate, self).form_valid(form)
