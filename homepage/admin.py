from django.contrib import admin

# Register your models here.

from .models import Stock

#admin.site.register(Stock)

class StockAdmin(admin.ModelAdmin):
    list_display = ('stockName', 'stockSymbol', 'candle_pattern', 'candle_trend', 's_and_r_trend', 'volume','volume_trend', 'macd_trend', 'rank')
admin.site.register(Stock, StockAdmin)
