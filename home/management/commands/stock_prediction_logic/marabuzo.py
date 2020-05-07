##final code for marobuzo recognition

# import threading
# import pandas as pd
# from queue import Queue
# import time
# file = open("stock_pred.txt", "w")
# data = pd.read_csv("C:\\Users\\BEST BUY\\Desktop\\NASDAQ_20200331.csv")
# symbols = data.iloc[:,0:1].values
# th = Queue(maxsize = 4000)

def marabuzo(arg):
    # print(i[0])
    # string = 'https://finnhub.io/api/v1/stock/candle?symbol='+ i[0] +'&resolution=D&count=1&token=bq24qknrh5rc5ioodhhg'
    # r = requests.get(string)
    # print(r.content)
    # if (str(r.headers.get('content-type'))) != "application/json; charset=utf-8":
    #     print("-----------------")
    #     th.put(threading.Thread(target=net_work, args = [i]))
    #     return
    c = arg['close']
    h = arg['high']
    l = arg['low']
    o = arg['open']
    if (c > o):
        if o != c:
            if ((((c-h)/c)*100) <= 0.5 and (((o-l)/o)*100) <= 0.5 and ((h-c)/(c-o)*100) <= 5 and ((o-l)/(c-o)*100) <= 5):
                return(2)
                # print("bullish Marabozu at " + str(i[0]))
                # file.write("bullish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o)+ " l = " + str(l) + "\n\n")
    else:
        if o != c:
            if ((((h-o)/o)*100) <= 0.5 and (((c-l)/c)*100)<= 0.5 and ((h-o)/(o-c)*100) <= 5 and ((c-l)/(o-c)*100) <= 5):
                return(0)
                # print("bearish Marabozu at " + str(i[0]))
                # file.write("bearish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o) + " l = " + str(l) + "\n\n")
    return(1)
