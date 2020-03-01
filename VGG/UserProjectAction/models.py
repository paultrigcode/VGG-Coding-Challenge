from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class UserProfile(models.Model):
    	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

class Project(models.Model):
	# id , name, description, completed ---> the model fields
	name = models.CharField(max_length=200, blank=False, unique=True)
	description = models.CharField(max_length=600, blank=False)
	completed = models.BooleanField()


class Action(models.Model):
	# id , project-id, description, notes ---> the model fields
	project_id = models.ForeignKey(Project, blank=False, on_delete=models.CASCADE)
	description = models.CharField(max_length=600, blank=False)
	notes = models.CharField(max_length=600, blank=False)



