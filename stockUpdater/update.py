from .stock_prediction_logic.analyse import start_analysis
from home.models import stocks

def updateStocks():
    # start_analysis()
    obj = stocks.objects.get(stockSymbol = "AAPL")
    obj.macd_trend = 'be'
    obj.rank = int(4)
    import datetime
    now = datetime.datetime.now()
    obj.volume = str(now)
    obj.save()
