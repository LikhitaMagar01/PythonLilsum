from django.contrib import admin
from .models import Workers
# Register your models here.
@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']