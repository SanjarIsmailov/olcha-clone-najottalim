from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Assuming you have a custom user model that inherits from AbstractBaseUser
CustomUser = get_user_model()

# Unregister the default User model from admin
admin.site.unregister(CustomUser)

# Register your custom user model with the custom UserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'groups']
    search_fields = ['username', 'email']
    ordering = ['username']

# Register the custom user admin
admin.site.register(CustomUser, CustomUserAdmin)
