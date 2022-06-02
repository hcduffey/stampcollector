from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Collection(models.Model):
    name = models.CharField(
        max_length=100
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

class Stamp(models.Model):
    name = models.CharField(
        max_length=100
    )

    cost = models.IntegerField(default=1)

    country = models.CharField(
        max_length=100
    )

    condition_choices = [("U","Used"), ("N","New")]
    condition = models.CharField(
        max_length = 15,
        choices = condition_choices,
        default = "New"
    )

    centering = models.CharField(
        max_length=100
    )

    format = models.CharField(
        max_length=100
    )

    image = models.CharField(
        max_length=100
    )

    year = models.IntegerField()

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="stamps")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
   

class Price(models.Model):
    source = models.CharField(
        max_length=100
    )

    stamps = models.ManyToManyField(Stamp)

    def __str__(self):
        return self.source

class Store(models.Model):
    name = models.CharField(
        max_length=100
    )

    url = models.CharField(
        max_length=100
    )

    stamps = models.ManyToManyField(Stamp)

    def __str__(self):
        return self.name
