from datetime import datetime
from django.db import models


# Create your models here.


class Short(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    bookmark = models.URLField()
    short_url = models.URLField()
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return str(self.short_url)


class Click(models.Model):
    clicker_ID = models.ForeignKey(User, blank=True, null=True)
    short_ID = models.ForeignKey(Short)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.id)
