from django.contrib import admin
from .models import ReadWorker

@admin.register(ReadWorker)
class ReadWorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
