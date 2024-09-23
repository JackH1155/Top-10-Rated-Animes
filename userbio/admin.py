from django.contrib import admin
from .models import UserBio


class UserBioAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_on')


# Register your models here.
admin.site.register(UserBio, UserBioAdmin)