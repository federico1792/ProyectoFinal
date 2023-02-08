from django.contrib import admin
from users.models import UserProfile, User

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'birth_date', 'profile_image')
    search_fields = ('user__username',)

