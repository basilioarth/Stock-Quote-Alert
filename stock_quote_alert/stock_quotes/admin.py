from django.contrib import admin
from .models import StockQuote, StockQuoteHist

admin.site.register(StockQuote)
admin.site.register(StockQuoteHist)
