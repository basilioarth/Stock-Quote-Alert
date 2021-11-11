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
    update_at =  models.DateTimeField(null=True)
    change_percent = models.FloatField()
    fk_stock_quote = models.ForeignKey('StockQuote', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.fk_stock_quote.name} ({self.fk_stock_quote.symbol}): {self.price}, {self.change_percent} - {self.update_at}"