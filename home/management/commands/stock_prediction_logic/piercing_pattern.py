# from trend import trend
# import requests
#print(trend("AAPL"))

####          check for the previous trend           ####
####    Downward trend required for this pattern     ####

    # string = 'https://finnhub.io/api/v1/stock/candle?symbol='+ "AAPL" +'&resolution=D&count=2&token=bq24qknrh5rc5ioodhhg'
    # r = requests.get(string)
    #print(len(r.json()['c']))
def piercing_pattern(arg):
    c0 = arg[1]['close']
    h0 = arg[1]['high']
    l0 = arg[1]['low']
    o0 = arg[1]['open']

    c1 = arg[0]['close']
    h1 = arg[0]['high']
    l1 = arg[0]['low']
    o1 = arg[0]['open']
    if( (c0 < o0) and (c1 > o1) ):
        if((c0 >= o1) and (c1 > c0) and (o0 >= c1)):
            if(((((c1-c0)/(o0-c0))*100)>50) and ((((c1-c0)/(o0-c0))*100)<100)):
                return(1)
        # elif( (c0 <= o1) and (o0 >= c1)):
        #     if(((((c1-o1)/(o0-c0))*100) > 50) and (((((c1-o1)/(o0-c0))*100) <100))):
        #         print("piercing pattern")


        #### This case is handled in the Bullish Harami ####
        ####       Make sure this works properly        ####


        elif((c0 <= o1) and (o1 < o0) and (c1 >= o0)):
            if(((((o0-o1)/(o0-c0))*100)>50) and (((((o0-o1)/(o0-c0))*100)< 100))):
                return(1)
    #file.write("bearish Marabozu at " + str(i[0])+ "\n" + " c = " + str(c) + " h = " + str(h)+ " o= " + str(o) + " l = " + str(l) + "\n\n")
    return(0)
