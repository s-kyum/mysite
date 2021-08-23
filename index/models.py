from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Room(models.Model):
    roomnumber = models.IntegerField()
    size = models.IntegerField()
    standard = models.IntegerField()
    max = models.IntegerField()
    peak = models.IntegerField()
    mid =models.IntegerField()
    off = models.IntegerField()

    def to_json(self):
        return {
            "roomnumber":self.roomnumber,
            "size":self.size,
            "standard":self.standard,
            "max":self.max,
            "peak":self.peak,
            "mid":self.mid,
            "off":self.off,
        }

