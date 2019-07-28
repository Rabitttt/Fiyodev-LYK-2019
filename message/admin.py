from django.contrib import admin
from .models import message
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(message)
class message(admin.ModelAdmin):
    list_display = ['sender','receiver','date','message']
    list_display_links = ['sender','receiver','date','message']
    search_fields = ['sender','receiver','date','message']
    class Meta:
        model=message
