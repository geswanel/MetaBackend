from typing import Any
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from . import models
# Register your models here.
#admin.site.register(models.Dish)
admin.site.register(models.Category)

admin.site.unregister(User)

@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True
        
        return form



@admin.register(models.Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')
    search_fields = ('title', 'price')