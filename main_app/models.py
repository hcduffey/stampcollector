from django.db import models

# Create your models here.

class Stamp(models.Model):
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
   
    