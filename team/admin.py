from django.contrib import admin
from .models import Team
from django.contrib.auth.admin import UserAdmin

@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ['name','owner','event_date','event_type','event_name']
    list_display_links = ['name','owner','event_date','event_type','event_name']
    search_fields = ['name','owner','event_date','event_type','event_name']


    class Meta:
        model = Team



# Register your models here.

