from django.db import models
from django.contrib.auth.models import User


class todoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        if len(self.task) > 50:
            return self.task[:50] + '....'
        else:
            return self.task
