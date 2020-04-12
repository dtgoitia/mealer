from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeIngredientInlineAdmin(admin.TabularInline):
    model = RecipeIngredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ("name", "preparation", "markdown")
    readonly_fields = ("markdown",)
    list_display = ("name", "duration")
    ordering = ("name",)
    inlines = (RecipeIngredientInlineAdmin,)
