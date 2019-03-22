from django.db import models

class userAccounts(models.Model):
    userName=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)