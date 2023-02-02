from django.contrib import admin

# Register your models here.
class KidsAdmin(admin.ModelAdmin):
    list_display = ['is', 'name', 'roll', 'city']