from django import forms
from team.models import Team



class TeamCreateForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = [
            'name',
            'event_name',
            'event_type',
            'event_information',
            'event_date',
        ]

"""
    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.name = self.name
        obj.owner = self.request.user
        obj.event_name = self.event_name
        obj.event_type = self.event_type
        obj.event_information = self.event_information
        obj.event_date = self.event_date
        obj.team_date = self.team_date

        obj.save(True)
"""