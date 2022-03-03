from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Moment(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    moment = models.ForeignKey(Moment, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for @{self.url}"