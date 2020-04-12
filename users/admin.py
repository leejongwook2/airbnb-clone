from django.contrib import admin
from . import models

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ CustomUser Admin Definition """

    list_display = (
        "username", "gender", "email", "language", "currency", "superhost"
    )

    list_filter = ('superhost','language',)