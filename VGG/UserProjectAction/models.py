from django.db import models

# Create your models here.

class User(models.Model):
	# id , name, description, completed ---> the model fields
	username = models.CharField(max_length=200, blank=False, unique=True)
	password = models.CharField(max_length=600, blank=False)
	

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



