from django.db import models


class Information(models.Model):
    place = models.CharField(max_length=20, default="-", name="place")
    sex = models.CharField(max_length=10, default="-", name="sex")
