from django.contrib import admin

from django.contrib import admin
from .models import Buyer, Game, Records


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)
    list_filter = ('balance', 'age',)
    fields = [('name', 'balance', 'age')]


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited')
    search_fields = ('title',)
    list_filter = ('cost', 'size', 'age_limited',)
    fieldsets = (
        ('Game Info', {
            'fields': (('title', 'cost'),)
        }),
        ('Game Description', {
            'fields': ('description', ('size', 'age_limited'),)
        }),
    )


@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'record')
    search_fields = ('title',)
    list_filter = ('name', 'record')
    fields = [('title', 'name', 'record')]
