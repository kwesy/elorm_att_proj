from django.db import models
from datetime import datetime
from user_profile.models import Profile

# Create your models here.


class Attendance(models.Model):
    finger_id = models.ForeignKey(Profile, to_field='finger_id', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)