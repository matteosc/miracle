from django.db import models

class Personnel(models.Model):
    name = models.CharField(max_length=80)
    qualifica = models.CharField(max_length=30)