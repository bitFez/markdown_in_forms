from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.q_title