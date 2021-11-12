from django.shortcuts import render
from .models import StockQuoteHist

def dashboard(request):
    stock_quotes = StockQuoteHist.objects.values()
    return render(request, "stock_quotes/dashboard.html", {"StockQuoteHist": stock_quotes})
