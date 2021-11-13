from django.contrib import admin

from .models import CustomUser, Announcement

admin.site.register(CustomUser)
admin.site.register(Announcement)
