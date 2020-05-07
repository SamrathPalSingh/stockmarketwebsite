# from trend import trend
# import requests
#print(trend("AAPL"))

####          check for the previous trend           ####
####    Downward trend required for this pattern     ####
from .doji import doji
def morning_star(arg):
    # string = 'https://finnhub.io/api/v1/stock/candle?symbol='+ "AAPL" +'&resolution=D&count=3&token=bq24qknrh5rc5ioodhhg'
    # r = requests.get(string)
    # print(len(r.json()['c']))

    c0 = arg[1]['close']
    h0 = arg[1]['high']
    l0 = arg[1]['low']
    o0 = arg[2]['open']

    c1 = arg[1]['close']
    h1 = arg[1]['high']
    l1 = arg[1]['low']
    o1 = arg[1]['open']

    c2 = arg[0]['close']
    h2 = arg[0]['high']
    l2 = arg[0]['low']
    o2 = arg[0]['open']

    if( (c0 < o0) and (c0 > o1) and (c1 < o2) and (c2 > o2) and (c2 > o0) ):
        if(not(doji(arg[2])) and (c0<o0)):
            if(doji(arg[1])):
        ###if( !doji( on day 1 ) ):
        ### if( doji( on day 2 ) ):
                return(1)

    #file.write("bearish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o) + " l = " + str(l) + "\n\n")
    return(0)
