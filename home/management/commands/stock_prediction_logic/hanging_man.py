# from trend import trend
# import requests
#print(trend("AAPL"))


####          check for the previous trend         ####
####    Upward trend required for this pattern     ####

##*****#####****   hanging man not as accurate in predicting as the hammer ****####****####
def hanging_man(arg):
    c = arg['close']
    h = arg['high']
    l = arg['low']
    o = arg['open']
    if (c > o):
        #print("up")
        if (((c-o) <= (2*(o-l))) and ((c-o) <= (0.075*((c+o)/2)))):
            return(1)
    else:
        if (((o-c) <= (2*(c-l))) and ((o-c) <= (0.075*((c+o)/2)))):
            return(1)
    return(0)
