import requests
def sr(sr_value, arg):
    #r = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/'+ str(sym) +'?timeseries=1')
    h = arg['high']
    l = arg['low']
    if(((abs(h-sr_value))/(sr_value)) < 0.075 ):
        return(1)
    elif(((abs(l-sr_value))/(sr_value)) < 0.075):
        return(1)
    else:
        return(0)
