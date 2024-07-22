from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100, default='Nazev')
    location = models.CharField(max_length=200, default='Location')
    description = models.TextField(max_length=200, default='No description provided')  # Přidání výchozí hodnoty

    def __str__(self):
        return self.name

