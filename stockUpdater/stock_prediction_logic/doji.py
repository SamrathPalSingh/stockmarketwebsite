# ## Complete Doji
# import threading
# import pandas as pd
# from queue import Queue
# import time
# import requests
# file = open("stock_pred.txt", "w")
# data = pd.read_csv("C:\\Users\\BEST BUY\\Desktop\\NASDAQ_20200331.csv")
# symbols = data.iloc[:100,0:1].values
# th = Queue(maxsize = 4000)

def doji(arg):
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
    if (c >= o):
        if( (c-o) <= (0.015*((c+o)/2)) ):
            return(1)
    else:
        if( (o-c) <= (0.015*((c+o)/2)) ):
            return(1)
    return(0)

# for i in symbols:
#     th.put(threading.Thread(target=net_work, args = [i]))
#
# while (th.qsize()) > 0:
#     print("-------------------iteration------------------------")
#     time.sleep(5)
#     temp = []
#     for j in range(0, 100):
#         if th.empty() == False:
#             temp1 = th.get()
#             temp.append(temp1)
#             temp1.start()
#     for i in temp:
#         i.join()
#
#
# file.close()
# print("END")
