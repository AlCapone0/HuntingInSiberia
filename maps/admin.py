from django.contrib import admin
from .models import Map

@admin.register(Map)
class AdminMap(admin.ModelAdmin):
    list_display = ["id", "name", "updated"]    #какие поля БД отображать в Админ сайте


