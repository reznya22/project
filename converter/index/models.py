from django.db import models


class Wallet(models.Model):
    bit_cost = models.FloatField(default=0, name="bit_cost")
    eth_cost = models.FloatField(default=0, name="eth_cost")
    usd_cost = models.FloatField(default=0, name="usd_cost")
    rub_cost = models.FloatField(default=0, name="rub_cost")
    byn_cost = models.FloatField(default=0, name="byn_cost")
    eur_cost = models.FloatField(default=0, name="eur_cost")
