# from trend import trend
# import requests
#print(trend("AAPL"))


####          check for the previous trend         ####
####    Upward trend required for this pattern     ####
def shooting_star(arg):
    # string = 'https://finnhub.io/api/v1/stock/candle?symbol='+ "AAPL" +'&resolution=D&count=1&token=bq24qknrh5rc5ioodhhg'
    # r = requests.get(string)
    #print(r.content)
    # if (str(r.headers.get('content-type'))) != "application/json; charset=utf-8":
    #     print("-----------------")
    #     th.put(threading.Thread(target=net_work, args = [i]))
    #     return
    c = arg['close']
    h = arg['high']
    l = arg['low']
    o = arg['open']
    if (c > o):
        if ( ((c-o) <= (2*(h-c))) and ((c-o) <= (0.075*((c+o)/2))) and ((o-l)/o <= 0.005) and ((o-l)/(c-o) <= 0.05) ):
            return(1)
                #file.write("bullish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o)+ " l = " + str(l) + "\n\n")
    else:
        if ( ((o-c) <= (2*(h-o))) and ((o-c) <= (0.075*((c+o)/2))) and ((c-l)/c <= 0.005) and ((c-l)/(o-c) <= 0.05) ):
            return(1)
                #file.write("bearish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o) + " l = " + str(l) + "\n\n")
    return(0)
