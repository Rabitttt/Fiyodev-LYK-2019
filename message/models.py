from django.db import models
from django.conf import settings
# Create your models here.

class message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='messages_from_me')
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='messages_to_me')
    message = models.TextField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)
