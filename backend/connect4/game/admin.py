from django.contrib import admin
from .models import Connect4Game


@admin.register(Connect4Game)
class CartItemAdmin(admin.ModelAdmin):
    list_display: list = ["id"]
