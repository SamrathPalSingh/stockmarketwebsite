import os, sys
sys.path.append('C:/Users/BEST BUY/Documents/django/stockmarketwebsite/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'stockmarketwebsite.settings'
import django
django.setup()
from home.models import stock
# from stock_prediction_logic.test import start_analysis
# start_analysis()
import pandas as pd
data = pd.read_csv("stocks_names.csv")
symbols = data.iloc[:,0:2].values
for i in symbols:
    record = stock(stockName = i[1], stockSymbol = i[0], s_and_r_trend = "n", volume_trend='n', macd_trend = "na", volume = "-", candle_pattern = 'na', candle_trend='na', rank=int(0))
    record.save()
    print(i[0] + " | " + i[1])

# import threading
# from queue import Queue
# import time
# symbols = [i.stockSymbol for i in Stock.objects.all()]
# print(symbols)

#import datetime
# now = datetime.datetime.now()
# print("--------------- Script Started at ------------------")
# print(now.strftime("--------------- %Y-%m-%d %H:%M:%S ----------------"))
