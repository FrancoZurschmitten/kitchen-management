from django.db import models
from django.utils.translation import gettext_lazy as _

from foods.models import Food


class Recipe(models.Model):
    name = models.CharField(_("Nombre"), max_length=150, unique=True)
    instructions = models.TextField(_("Instrucciones"), blank=True, null=True)
    duration = models.IntegerField(_("Duración"), blank=True, null=True)
    ingredients = models.ManyToManyField(Food)

    def __str__(self):
        return self.name
