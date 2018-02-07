from django.contrib import admin

# Register your models here.

from home.models import UserProfile

admin.site.register(UserProfile)
