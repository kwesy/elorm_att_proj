from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your tests here.


class Record(models.Model):
    member_id = models.ManyToManyField(User)
    timestamp = models.DateTimeField(default=datetime.now)