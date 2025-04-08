from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# You can customize the User model here
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)

    # Fields for user creation and modification
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),  # Add custom fields here if needed
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),  # Add custom fields here if needed
    )

# Register the custom User admin
admin.site.register(User, CustomUserAdmin)
