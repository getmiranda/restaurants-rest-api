from django.db import models


class Restaurant(models.Model):
    """Database model for restaurants in the system"""
    id = models.CharField(
        max_length=36,
        primary_key=True,
        null=False,
        unique=True
    )
    rating = models.IntegerField()
    name = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        """Return string representation of our restaurant"""
        return self.name
