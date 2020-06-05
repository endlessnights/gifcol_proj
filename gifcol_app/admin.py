from django.contrib import admin
from .models import mediamodel, UserProfile


# Register your models here.

@admin.register(mediamodel)
class PublishAdmin(admin.ModelAdmin):
    list_display = ['author','title','desc','filetype','created_date']


admin.site.site_header = 'Gif Collection admin page'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'userdesc', 'userwebsite', 'avatar', 'cover']

   # def user_info(self, obj):
   #     return obj.userdesc

admin.site.register(UserProfile, UserProfileAdmin)