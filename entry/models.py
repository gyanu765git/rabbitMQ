from django.db import models

# Create your models here.

class CollectData(models.Model):
    record = models.JSONField(null=True, blank=True)


    # def __str__(self):
    #     return self.record

