from django.db import models


# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=500, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
