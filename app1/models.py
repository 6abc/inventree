from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='inventory/', blank=True, null=True)

    def __str__(self):
        return self.name