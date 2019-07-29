from django.db import models
from  django.contrib.auth.models import AbstractUser

# Create your models here.

class UserTable(AbstractUser):
    telephone = models.CharField(max_length=11, null=True, blank=True, verbose_name='deneme')
    birthday = models.DateTimeField(null=True,blank=True)
    location = models.CharField(null=True, max_length=20, blank=False)
    profile_picture = models.ImageField(null=True, blank=True)
    biography = models.TextField(null=True, max_length=500, blank=True)
    star = models.FloatField(null=True,blank=True)
    social_media = models.URLField(max_length=50)
    skills = models.TextField(null=False, blank=False, max_length=100)
    #Like_id =  Hocaya Sorulacak.(Diger kullanıcıları id leri nasıl tutulmalı.)
    #gpg_key = models.CharField(max_length=300,null=False, blank=False)

