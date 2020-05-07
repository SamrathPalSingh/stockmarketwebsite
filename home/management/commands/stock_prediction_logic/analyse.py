from .trend import trend
from .volume import volume
from .macd import macd
from .sr import sr
from .candle import candle
from home.models import stock
import requests
import threading
import pandas as pd
from queue import Queue
import time


th = Queue(maxsize = 4000)


def analyse(sym):
    #network calls check with try statemant
    print("Working on : " + str(sym))
    r = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/'+ str(sym) +'?timeseries=226')#network financialmodelingprep
    s = requests.get('https://finnhub.io/api/v1/scan/support-resistance?symbol='+ str(sym) +'&resolution=D&token=bq24qknrh5rc5ioodhhg')
    try:
        json_object = r.json()['historical'][:226]
        json_object = s.json()['levels'][-1]
    except:
        obj = stock.objects.get(stockSymbol = sym)
        obj.s_and_r_trend = "n"
        obj.volume_trend='n'
        obj.macd_trend = "na"
        obj.volume = "-"
        obj.candle_pattern = 'na'
        obj.candle_trend='na'
        obj.rank=int(0)
        obj.save()
        if( (str(r) == '<Response [429]>') and (str(s) == '<Response [200]>') ):
            th.put(str(sym))
            print("----------- Too many requests --------------")
        elif( (str(r) == '<Response [200]>') and (str(s) == '<Response [429]>' )):
            th.put(str(sym))
            print("----------- Too many requests --------------")
        elif( (str(r) == '<Response [429]>') and (str(s) == '<Response [429]>' )):
            th.put(str(sym))
            print("----------- Too many requests --------------")
        else:
            print("----------- something went wrong --------------")
        #th.put(threading.Thread(target=analyse, args = [sym]))
        return(0)

    sr_value = s.json()['levels'][-1]

    obj = stock.objects.get(stockSymbol = sym)

    # S&R
    arg = r.json()['historical'][0]
    sr_pattern = sr(sr_value, arg)
    if(sr_pattern == 1):
        #print('reversal') # save in the database
        obj.s_and_r_trend = 'y'
    else:
        obj.s_and_r_trend = 'n'
        #print('no reversal') # save in the database

    #trends
    trend_pattern_key = ('bearish', 'neutral' , 'bullish')
    arg =  [i['close'] for i in r.json()['historical'][:30]]
    trend_pattern = (trend(arg))

    # check for candle_pattern
    candle_pattern = candle(r.json()['historical'][:10], trend_pattern, 0)
    if(candle_pattern[0] == 0):
        obj.candle_trend = 'be'
        obj.candle_pattern = candle_pattern[1]
        #print('bearish')
    elif(candle_pattern[0] == 1):
        obj.candle_trend = 'na'
        obj.candle_pattern = candle_pattern[1]
        #print('neutral')
    elif(candle_pattern[0] == 2):
        obj.candle_trend = 'bu'
        obj.candle_pattern = candle_pattern[1]
        #print('bullish')
######## handle pattern followed by doji situation

    #volume
    arg1 = [float(i['volume']) for i in r.json()['historical'][1:10]]
    arg2 = float(r.json()['historical'][0]['volume'])
    obj.volume = str(arg2)
    volume_pattern = volume(arg1, arg2)
    if(volume_pattern == 0):
        obj.volume_trend = 'n'
        #print('avg')  # save in the database
    elif(volume_pattern == 1):
        obj.volume_trend = 'y'
        #print('abv/below avg') # save in the database


    #indicators
    macd_pattern = macd(r)
    if(macd_pattern == 0):
        obj.macd_trend = 'be'
        #print('bearish') # save in the database
    elif(macd_pattern == 1):
        obj.macd_trend = 'na'
        #print('neutral') # save in the database
    elif(macd_pattern == 2):
        obj.macd_trend = 'bu'
        #print('bullish') # save in the database

    #final logic to add the rank variable in the Stock model

    if( (candle_pattern[0] == macd_pattern) and (candle_pattern[0] != 1) and (macd_pattern != 1) and (volume_pattern == 1) and (sr_pattern == 1) ):
        obj.rank = int(4)
    elif( (candle_pattern[0] != macd_pattern) and (candle_pattern[0] != 1) and  (volume_pattern == 1) and (sr_pattern == 1) ):
        obj.rank = int(3)
    elif( (candle_pattern[0] == macd_pattern) and (candle_pattern[0] != 1) and (macd_pattern != 1) and (volume_pattern == 0) and (sr_pattern == 1) ):
        obj.rank = int(2)
    elif ( (candle_pattern[0] != macd_pattern) and (candle_pattern[0] != 1) and (volume_pattern == 0) and (sr_pattern == 1) ):
        obj.rank = int(1)
    else:
        obj.rank = int(0)
    obj.save()
    print("Working finised on : " + str(sym))

################################################################
#####################   driver code  ###########################
################################################################
def start_analysis():
    symbols = [i.stockSymbol for i in stock.objects.all()]
    for i in symbols:
        th.put(i)
    import datetime
    now = datetime.datetime.now()
    print("--------------- Script Started at ------------------")
    print(now.strftime("--------------- %Y-%m-%d %H:%M:%S ----------------"))

    while (th.qsize()) > 0:
        analyse(th.get())

    # symbols = [i.stockSymbol for i in Stock.objects.all()]
    # for i in symbols:
    #     th.put(threading.Thread(target=analyse, args = [i]))
    #
    # import datetime
    # now = datetime.datetime.now()
    # print("--------------- Script Started at ------------------")
    # print(now.strftime("--------------- %Y-%m-%d %H:%M:%S ----------------"))
    #
    # while (th.qsize()) > 0:
    #     time.sleep(20)
    #     print("-------------------NEW iteration started at ------------------------")
    #     now = datetime.datetime.now()
    #     print(now.strftime("--------------- %Y-%m-%d %H:%M:%S ----------------"))
    #     temp = []
    #     for j in range(0, 500):
    #         if th.empty() == False:
    #             temp1 = th.get()
    #             temp.append(temp1)
    #             temp1.start()
    #     for i in temp:
    #         i.join()
    #     print("------------------- iteration finished at------------------------")
    #     now = datetime.datetime.now()
    #     print(now.strftime("--------------- %Y-%m-%d %H:%M:%S ----------------"))
    #

    print("--------------END---------------")
    now = datetime.datetime.now()
    print(now.strftime("--------------- %Y-%m-%d %H:%M:%S ----------------"))
################################################################
#####################   Test   code  ###########################
################################################################
def test():
    obj = stock.objects.get(stockSymbol = "AAPL")
    obj.s_and_r_trend = "n"
    obj.volume_trend='n'
    obj.macd_trend = "na"
    obj.volume = "127346"
    obj.candle_pattern = 'na'
    obj.candle_trend='na'
    obj.rank=int(3)
    obj.save()
