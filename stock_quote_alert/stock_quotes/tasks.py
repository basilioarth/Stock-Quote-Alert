from apscheduler.schedulers.background import BackgroundScheduler
from django.shortcuts import get_object_or_404
from .models import StockQuote, StockQuoteHist
from users.models import User, UsersStockQuotes
from django.utils import timezone
from django.core.mail import send_mail
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def update_stock_quotes():
    stock_quotes_list = StockQuote.objects.values()
    users_stock_quotes = UsersStockQuotes.objects.values()

    for stock_quote in stock_quotes_list:
        stock_quote_id = stock_quote['id']
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
            fk_stock_quote = get_object_or_404(StockQuote, pk=stock_quote_id)
        )
        
        print("\nHistórico do ativo {} atualizado".format(symbol))

        for user_stock_quote in users_stock_quotes:
            if user_stock_quote['stock_quote_id'] == stock_quote_id:

                if current_price < user_stock_quote['inferior_limit']:

                    subject = "Sugestão de compra do ativo {}!".format(symbol)
                    message = "Olá, {} {}. Tudo bem?\n\nEstivemos monitorando o ativo do(a) {} para você e nós da Inoa detectamos uma oportunidade de compra!\n\nDesejamos sucesso em suas operações.\n\nAtenciosamente, Equipe Alpha | Inoa.".format(
                        get_object_or_404(User, pk=user_stock_quote['user_id']).first_name, 
                        get_object_or_404(User, pk=user_stock_quote['user_id']).last_name, 
                        stock_quote['name'])

                    send_mail(subject, message, os.environ.get('EMAIL_HOST_USER'), [get_object_or_404(User, pk=user_stock_quote['user_id']).email], fail_silently=False)
                    print("E-mail de sugestão de compra enviado para {} {}!".format(get_object_or_404(User, pk=user_stock_quote['user_id']).first_name, get_object_or_404(User, pk=user_stock_quote['user_id']).last_name))

                if current_price > user_stock_quote['upper_limit']:

                    subject = "Sugestão de venda do ativo {}!".format(symbol)
                    message = "Olá, {} {}. Tudo bem? \n\nEstivemos monitorando o ativo do(a) {} para você e nós da Inoa detectamos uma oportunidade de venda!\n\nDesejamos sucesso em suas operações.\n\nAtenciosamente, Equipe Alpha | Inoa.".format(
                        get_object_or_404(User, pk=user_stock_quote['user_id']).first_name, 
                        get_object_or_404(User, pk=user_stock_quote['user_id']).last_name, 
                        stock_quote['name'])

                    send_mail(subject, message, os.environ.get('EMAIL_HOST_USER'), [get_object_or_404(User, pk=user_stock_quote['user_id']).email], fail_silently=False)
                    print("E-mail de sugestão de venda enviado para {} {}!\n".format(get_object_or_404(User, pk=user_stock_quote['user_id']).first_name, get_object_or_404(User, pk=user_stock_quote['user_id']).last_name))
        

def start():
    scheduler = BackgroundScheduler(timezone="Europe/Berlin")
    scheduler.add_job(update_stock_quotes, "interval", minutes = 1)
    scheduler.start()