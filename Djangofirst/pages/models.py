from django.db import models
from django.shortcuts import render

# Create your models here.
class todolist(models.Model):
	content = models.TextField()
