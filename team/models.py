from django.conf import settings
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    event_date = models.DateTimeField(auto_now=True)
    event_type = models.CharField(max_length=50)
    event_name = models.CharField(max_length=30)
    event_information = models.TextField(max_length=500)




