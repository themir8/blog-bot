from django import db
from django.contrib import admin

from .models import BotUser


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', "username", "first_name",
                    'last_name', "phone")
    list_display_links = ('user_id',)
    search_fields = ('user_id', "username", "first_name",
                     'last_name', "phone")
    readonly_fields = ('date_joined',)
    list_filter = ('date_joined', 'ban', 'is_active')
    save_as = True
