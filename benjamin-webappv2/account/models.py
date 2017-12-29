from django.db import models
# Create your models here.


class account(models.Model):
    userId = models.CharField(max_length=30) # a unique id
    username = models.CharField(max_length=32) # not unique
    discriminator = models.CharField(max_length=4) # 4 digits
    avatar = models.CharField(max_length=100) # identifier of image
    token = models.CharField(max_length=50) # updates every login
    guilds = models.CharField(max_length=500) # encoded in json

class guilds(models.Model):
    guildId = models.CharField(max_length=30) # a unique id
    icon = models.CharField(max_length=100) # url to icon image
    settings = models.CharField(max_length=500) # all settings in a dict