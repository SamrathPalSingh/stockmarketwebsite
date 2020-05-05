import requests
def macd(s):
    r = s
    #for 26 day period
    lst = [ i['close'] for i in r.json()['historical'][-26:]]
    #print("len(lst) " + str(len(lst)))
    xn0 = sum(lst)/len(lst)
    lst = [ i['close'] for i in r.json()['historical'][:-26]]
    lst.reverse()
    k = 2/(26+1)
    ema26y = [ xn0 ]
    for i in lst:
        xn1 = (((i-xn0)*k)+xn0)
        ema26y.append(xn1)
        xn0 = xn1

    #for 12 day period
    lst = [ i['close'] for i in r.json()['historical'][-26:-14]]
    #print("len(lst) " + str(len(lst)))
    xn0 = sum(lst)/len(lst)
    lst = [ i['close'] for i in r.json()['historical'][:-26]]
    lst.reverse()
    k = 2/(12+1)
    ema12y = [ xn0 ]
    for i in lst:
        xn1 = (((i-xn0)*k)+xn0)
        ema12y.append(xn1)
        xn0 = xn1

    #macd = [(l-k) for l in ema12y, k in ema26y]
    #print(str(len(ema12y)))
    #print(str(len(ema26y)))
    macd = []
    for i in range(len(ema26y)):
        macd.append(ema12y[i]-ema26y[i])

    #for 9 day period (signal line)
    lst = macd[-9:]
    #print("len(lst) " + str(len(lst)))
    xn0 = sum(lst)/len(lst)
    lst = macd[:-9]
    k = 2/(9+1)
    sigy = [ xn0 ]
    for i in lst:
        xn1 = (((i-xn0)*k)+xn0)
        sigy.append(xn1)
        xn0 = xn1

    # print("sigy[-1]" + str(sigy[-1]))
    # print("sigy[-2]" + str(sigy[-2]))
    # print("macd[-1]" + str(macd[-1]))
    # print("macd[-2]" + str(macd[-2]))

    if( ((sigy[-1] - macd[-1]) > 0) and ((sigy[-2] - macd[-2])< 0) ):
        #print("bearish")
        return(2)
    elif( ((sigy[-1] - macd[-1]) < 0) and ((sigy[-2] - macd[-2]) > 0) ):
        #print("bullish")
        return(0)
    else:
        #print("neutral")
        return(1)
