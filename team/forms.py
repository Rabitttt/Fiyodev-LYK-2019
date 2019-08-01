from django import forms
from team.models import Team


class RealDateInput(forms.DateInput):
    input_type='date'

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
        widgets={'event_date':RealDateInput}

