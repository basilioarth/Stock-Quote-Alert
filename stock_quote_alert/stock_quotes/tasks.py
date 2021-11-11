from apscheduler.schedulers.background import BackgroundScheduler
from django.shortcuts import redirect, render, get_object_or_404

from .models import StockQuote, StockQuoteHist

from django.utils import timezone

import requests

def update_stock_quotes():
    stock_quotes_list = StockQuote.objects.values()

    
    for stock_quote in stock_quotes_list:
        id_fk = stock_quote['id']
        symbol = stock_quote['symbol']

        url = 'https://api.hgbrasil.com/finance/stock_price?key=d482be5d&symbol=' + symbol
        request_result = requests.get(url).json()

        current_price = request_result['results'][symbol]['price']
        change_percent = request_result['results'][symbol]['change_percent']
        updated_by_api_at = request_result['results'][symbol]['updated_at']

        StockQuoteHist.objects.create(
            price = current_price,
            change_percent = change_percent,
            updated_by_api_at = updated_by_api_at,
            last_consult_at = timezone.now(),
            fk_stock_quote = get_object_or_404(StockQuote, pk=id_fk)
        )
        print("\nHistórico de todos os ativos atualizado\n")
    

def start():
    scheduler = BackgroundScheduler(timezone="Europe/Berlin")
    scheduler.add_job(update_stock_quotes, "interval", minutes = 1)
    scheduler.start()