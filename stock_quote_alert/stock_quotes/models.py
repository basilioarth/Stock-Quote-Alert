from django.db import models

class StockQuote(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True)
    region = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"
    
class StockQuoteHist(models.Model):
    price = models.FloatField()
    change_percent = models.FloatField()
    updated_by_api_at =  models.DateTimeField(null=True, auto_now_add=True)
    last_consult_at =  models.DateTimeField(null=True, auto_now_add=True)
    fk_stock_quote = models.ForeignKey('StockQuote', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.fk_stock_quote.name} ({self.fk_stock_quote.symbol}): {self.price}, {self.change_percent} - {self.last_consult_at}"