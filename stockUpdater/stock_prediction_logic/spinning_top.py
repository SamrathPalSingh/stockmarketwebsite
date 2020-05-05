#data required : 1 day
def spinning_top(arg):
    c = arg['close']
    h = arg['high']
    l = arg['low']
    o = arg['open']
    if (c >= o):
        #print("up")
        flag1 = 0
        if( (h-c) > (o-l) ):
            if( (h-c) <= (o-l)*1.2 ):
                flag1 = 1
        elif ( (h-c) < (o-l) ):
            if( (h-c)*1.2 >= (o-l) ):
                flag1 = 1
        elif ( (h-c) == (o-l) ):
                flag1 = 1
        flag2 = 0
        if( (c-o) <= (0.03*((c+o)/2)) ):
                flag2 = 1
        if( flag1 == 1 and flag2 == 1):
            return(1)
    else:
        flag1 = 0
        if( (h-o) > (c-l) ):
            if( (h-o) <= (c-l)*1.2 ):
                flag1 = 1
        elif ( (h-o) < (c-l) ):
            if( (h-o)*1.2 >= (c-l) ):
                flag1 = 1
        elif ( (h-o) == (c-l) ):
                flag1 = 1
        flag2 = 0
        if( (o-c) <= (0.03*((c+o)/2)) ):
            flag2 = 1
        if( flag1 == 1 and flag2 == 1):
            return(1)
    return(0)
