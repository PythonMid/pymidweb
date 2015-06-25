from django.contrib import admin
from pythonmid.apps.community.models import Sponsor, UserProfile


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'website', 'logo')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image', 'is_member')
