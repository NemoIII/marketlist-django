from django.contrib import admin
from .models import MarketList

# Register your models here.
class MarketListAdmin(admin.ModelAdmin):
    list_display = ("title", "completed")

admin.site.register(MarketList, MarketListAdmin)