from django.contrib import admin

from game.models import Player, Skill


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    fields = ['name', 'level', 'user', 'skills']


@admin.register(Skill)
class PlayerAdmin(admin.ModelAdmin):
    fields = ['name', 'level', 'description', 'exp']