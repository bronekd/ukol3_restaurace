from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField(default='No description provided')  # Přidání výchozí hodnoty

    def __str__(self):
        return self.name

