from django.db import models

# Create your models here.

class comment(models.Model):

    created_at=models.DateTimeField(auto_now_add=True)
    updates_at=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=25)
    content=models.TextField()
