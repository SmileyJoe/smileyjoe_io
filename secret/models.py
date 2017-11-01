from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class Secret(models.Model):
    hash = models.CharField(max_length=32)
    secret = models.CharField(max_length=256)
    expires = models.DateTimeField(default=datetime.now()+timedelta(days=3))

    def __str__(self):
        return self.secret
