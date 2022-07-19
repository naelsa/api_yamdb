from django.contrib import admin


class CustomEmptyMixin(admin.ModelAdmin):
    """Кастомный миксин для пустого поля."""
    empty_value_display = '-пусто-'
