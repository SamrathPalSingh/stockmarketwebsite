# from trend import trend
# import requests
#print(trend("AAPL"))

####          check for the previous trend         ####
####    Downward trend required for this pattern     ####
def bullish_engulfing(arg):
    # string = 'https://finnhub.io/api/v1/stock/candle?symbol='+ "AAPL" +'&resolution=D&count=2&token=bq24qknrh5rc5ioodhhg'
    # r = requests.get(string)
    #print(len(r.json()['c']))

    c0 = arg[1]['close']
    h0 = arg[1]['high']
    l0 = arg[1]['low']
    o0 = arg[1]['open']

    c1 = arg[0]['close']
    h1 = arg[0]['high']
    l1 = arg[0]['low']
    o1 = arg[0]['open']
    if( (c0 < o0) and ( (c1 > o0) and (o1 < c0) ) and (c1 > o1)):
        return(1)
    return(0)
#file.write("bearish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o) + " l = " + str(l) + "\n\n")
