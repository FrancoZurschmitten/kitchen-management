from django.contrib import admin
from .models import Vegetable, Carbohydrate, Protein, Fruit

admin.site.register([Vegetable, Carbohydrate, Protein, Fruit])
