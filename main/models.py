# main/models.py

from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
