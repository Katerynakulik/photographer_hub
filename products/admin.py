from django.contrib import admin
from .models import PhotoProduct

@admin.register(PhotoProduct)
class PhotoProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}