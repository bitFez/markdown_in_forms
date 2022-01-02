from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    # Changed the field below from Textfield to MarkdownxField
    content = MarkdownxField() #models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.q_title