from django.db import models


class User(models.Model):
    login = models.CharField(max_length=20, name="login")
    email = models.EmailField("user email adress")
