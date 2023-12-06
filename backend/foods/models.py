from django.db import models
from django.utils.translation import gettext_lazy as _


class FoodBaseAbstract(models.Model):
    name = models.CharField(_("Nombre"), max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Vegetable(FoodBaseAbstract):
    pass


class Protein(FoodBaseAbstract):
    pass


class Carbohydrate(FoodBaseAbstract):
    pass


class Fruit(FoodBaseAbstract):
    pass
