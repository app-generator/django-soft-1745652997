# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Audio(models.Model):

    #__Audio_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Audio_FIELDS__END

    class Meta:
        verbose_name        = _("Audio")
        verbose_name_plural = _("Audio")


class Activity(models.Model):

    #__Activity_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Activity_FIELDS__END

    class Meta:
        verbose_name        = _("Activity")
        verbose_name_plural = _("Activity")


class Directory(models.Model):

    #__Directory_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Directory_FIELDS__END

    class Meta:
        verbose_name        = _("Directory")
        verbose_name_plural = _("Directory")



#__MODELS__END
