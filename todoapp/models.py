from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Define to_do model

class Todo(models.Model):
	text = models.CharField(max_length=250)
	is_complete = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete = models.CASCADE, blank = False, null = False) # models.CASCADE --> means if the user gets deleted delete the models
	
	def __str__(self):
		return self.text