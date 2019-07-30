from django import forms
from team.models import Team


class TeamCreateForm(forms.Form):

    class Meta:
        model = Team
        fields = [
            'name',
            'event_name',
            'event_type',
            'event_information',
            'event_date',
        ]
