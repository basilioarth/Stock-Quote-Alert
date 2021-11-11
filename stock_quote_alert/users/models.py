from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from django.db import models

from gm2m import GM2MField

class User(AbstractUser):
    stockQuotes = GM2MField("stock_quotes.StockQuote", through='UsersStockQuotes', related_name='users')

class UsersStockQuotes(models.Model):
    # modeling base fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_quote = GenericForeignKey('stock_quote_ct', 'stock_quote_id')
    stock_quote_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    stock_quote_id = models.PositiveIntegerField()
    # extra fields
    inferior_limit = models.FloatField()
    upper_limit = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.stock_quote.name} ({self.stock_quote.symbol}): limite inferior: {self.inferior_limit} | limite superior: {self.upper_limit}"