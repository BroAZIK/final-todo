from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
   title       = models.CharField(max_length=200)
   completed   = models.BooleanField(default=False)
   description = models.TextField(default='', blank=True)
   created     = models.DateTimeField(auto_now_add=True)
   user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')


   def __str__(self):
       return f"{self.id}. {self.title} is {self.description}  created at {self.created.strftime('%d.%m.%Y')}"