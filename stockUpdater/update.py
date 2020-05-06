from .stock_prediction_logic.analyse import start_analysis
from home.models import stocks
def updateStocks():
    # start_analysis()
    obj = stock.objects.get(stockSymbol = "AAPL")
    obj.macd_trend = 'be'
    obj.rank = int(4)
    obj.save()
