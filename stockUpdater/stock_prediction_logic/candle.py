from .spinning_top import spinning_top
from .bearish_harami import bearish_harami
from .bearish_engulfing import bearish_engulfing
from .bullish_engulfing import bullish_engulfing
from .bullish_harami import bullish_harami
from .dark_cloud_cover import dark_cloud_cover
from .doji import doji
from .evening_star import evening_star
from .hammer import hammer
from .hanging_man import hanging_man
from .marabuzo import marabuzo
from .morning_star import morning_star
from .piercing_pattern import piercing_pattern
from .shooting_star import shooting_star
def candle(arg, trend_pattern, flag):
    #print("incandle")
    if(flag == 7):
        return([1, 'd'])
    if(trend_pattern == 2 ):# upward required
        #print("hello1")
        if(bearish_harami(arg[flag:flag+2]) == 1):
            return([0, 'behar'])
        if(bearish_engulfing(arg[flag:flag+2]) == 1):
            return([0, 'beeng'])
        if(dark_cloud_cover(arg[flag:flag+2]) == 1):
            return([0, 'dcc'])
        if(evening_star(arg[flag:flag+3]) == 1):
            return([0, 'es'])
        if(hanging_man(arg[flag+0]) == 1):
            return([0, 'hm'])
        if(shooting_star(arg[flag+0]) == 1):
            return([0, 'ss'])
    if(trend_pattern == 0 ):# downward required
        #print("hello2")
        if(bullish_engulfing(arg[flag:flag+2]) == 1):
            return([2, 'bueng'])
        if(bullish_harami(arg[flag:flag+2]) == 1):
            return([2, 'buhar'])
        if(hammer(arg[flag+0]) == 1):
            return([2, 'h'])
        if(morning_star(arg[flag:flag+3]) == 1):
            return([2, 'ms'])
        if(piercing_pattern(arg[flag:flag+2]) == 1):
            return([2, 'pp'])
    if(spinning_top(arg[flag+0]) == 1):
        #print("insp")
        return([1, 'st'])
    if(marabuzo(arg[flag+0]) == 0):
        return([0, 'bemar'])
    elif(marabuzo(arg[flag+0]) == 2):
        return([2, 'bumar'])
    doji_pattern = doji(arg[flag+0])
    if((doji_pattern == 1) and (flag < 7)):
        #print("indoji")
        return(candle(arg, trend_pattern, flag+1))
    #print("nothing")
    return([1, 'na'])
