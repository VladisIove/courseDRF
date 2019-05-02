from django.db import models
from django.contrib.auth.models import AbstractUser
from course.models import Course 
# Create your models here.

class CustomUser( AbstractUser ):
	name = models.CharField(blank=True, max_length=255)
	boughtCourse = models.ManyToManyField(Course)

	def __str__(self):
		return 'Name: {}, e-mail: {}'.format(self.name, self.email )
