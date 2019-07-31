from django.conf import settings
from django.db import models




# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    team_date = models.DateTimeField(auto_now=True)
    event_type = models.CharField(max_length=50)
    event_name = models.CharField(max_length=30)
    event_information = models.TextField(max_length=500)
    event_date = models.DateTimeField(null=True,blank=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL,through='participants')

"""

class TeamManager(models.Manager):
    #use_for_related_fields = True

    def add_player(self , participant , team ):
        pass

    def remove_player(self , participant , team):
        pass

"""

class Participants(models.Model):
    participant = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

