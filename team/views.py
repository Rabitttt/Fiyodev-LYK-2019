from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView
from team.forms import TeamCreateForm, InvitePlayerForm
from users.models import UserTable
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

"""
class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    form_class = TeamUpdateForm
    pk_url_kwarg = "team_id"

    def get_success_url(self):
        return reverse("team_detail", kwargs={"event_id": self.kwargs["event_id"], "team_id": self.object.id})
"""

class TeamAddUser(UpdateView):
    form_class = InvitePlayerForm
    url = reverse_lazy("teamlist")
    template_name = "user_add_team.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            user = request.objects.get(id=form.cleaned_data["id"])
            self.request.team.participant.add(user)
            return HttpResponseRedirect(self.url)
        else:
            return HttpResponseRedirect(form.errors)

