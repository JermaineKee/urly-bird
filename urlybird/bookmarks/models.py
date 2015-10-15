from django.db import models

# Create your models here.
class Short(models.Model):
    user = models.ForeignKey(User)
    # bookmark
    # short_url
    # timestamp
    # title
    # description
