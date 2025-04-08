from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()

admin.site.unregister(CustomUser)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'groups']
    search_fields = ['username', 'email']
    ordering = ['username']

admin.site.register(CustomUser, CustomUserAdmin)
