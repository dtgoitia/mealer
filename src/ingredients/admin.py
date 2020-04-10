from django.contrib import admin

from .models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    fields = ("name", "unit")
    list_display = ("name",)
    ordering = ("name",)


admin.site.register(Ingredient, IngredientAdmin)
