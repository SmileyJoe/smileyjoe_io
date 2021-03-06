from django.db import models
from datetime import datetime, timedelta
from secret import constant


# Create your models here.
class Secret(models.Model):
    id = models.CharField(max_length=6, unique=True, primary_key=True)
    secret = models.CharField(max_length=constant.SECRET_MAX_LENGTH)
    expires = models.DateTimeField(default=datetime.now()+timedelta(days=3))

    def __str__(self):
        return self.secret
