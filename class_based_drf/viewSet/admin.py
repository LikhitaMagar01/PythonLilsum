from django.contrib import admin
from .models import Family

# Register your models here.
@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'roll', 'city']