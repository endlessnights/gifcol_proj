from django.contrib import admin
from .models import mediamodel
# Register your models here.

@admin.register(mediamodel)
class PublishAdmin(admin.ModelAdmin):
    list_display = ['author','title','desc','filetype','created_date']
