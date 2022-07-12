from django.contrib import admin
from .models import User


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'bio', 'confirmation_code', 'role')


admin.site.register(User, CustomUserAdmin)
