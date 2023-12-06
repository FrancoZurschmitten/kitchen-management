from django.db import models
from django.utils.translation import gettext_lazy as _


class Food(models.Model):
    class GroupFood(models.IntegerChoices):
        PROTEIN = 0, _("Proteina")
        CARBOHYDRATE = 1, _("Carbohidrato")
        VEGETABLE = 2, _("Vegetal")
        DAIRY = 3, _("Lacteo")
        FRUIT = 4, _("Fruta")

    name = models.CharField(max_length=150)
    group = models.IntegerField(
        choices=GroupFood.choices, default=GroupFood.PROTEIN)
    brand = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        group = self.GroupFood.labels[self.group]
        return f"{self.name} | {group}"
