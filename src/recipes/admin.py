from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeIngredientInlineAdmin(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    fields = ("name", "preparation")
    list_display = ("name",)
    ordering = ("name",)
    inlines = (RecipeIngredientInlineAdmin,)


admin.site.register(Recipe, RecipeAdmin)
