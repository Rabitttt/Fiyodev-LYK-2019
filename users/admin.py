from django.contrib import admin
from .models import UserTable
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(UserTable)
class UserTable(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
                ('Custom Fields', {'fields': ('telephone', 'birthday', 'location', 'profile_picture', 'biography','social_media','star','skills')}),
    )