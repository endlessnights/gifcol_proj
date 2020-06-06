from django.contrib import admin
from .models import Meme, Tag

admin.site.site_header = 'Gif Collection admin page'


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'published', 'created_at')
    autocomplete_fields = ('tags', )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',  'created_at')
    search_fields = ('title', )
    readonly_fields = ('created_at', 'updated_at')
