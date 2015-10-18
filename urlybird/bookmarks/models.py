from datetime import datetime
from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Short(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    bookmark = models.URLField()
    short_url = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    click_count = models.IntegerField()

    def __str__(self):
        return str(self.short_url)


class Click(models.Model):
    clicker = models.ForeignKey(User, blank=True, null=True)
    short = models.ForeignKey(Short)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.id)
