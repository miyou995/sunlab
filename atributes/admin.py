from django.contrib import admin

from .models import  Cheveux, Tag, Parfum

@admin.register(Cheveux)
class CheveuxAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Parfum)
class ParfumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

