from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    finger_id = models.IntegerField(unique=True)
    index_no = models.TextField()
    programme = models.TextField()

