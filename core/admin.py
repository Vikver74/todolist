from django.contrib import admin

from core.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', )
    search_fields = ('email', 'first_name', 'last_name', 'user_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('date_joined', 'last_login')
    exclude = ['password']


admin.site.register(User, UserAdmin)