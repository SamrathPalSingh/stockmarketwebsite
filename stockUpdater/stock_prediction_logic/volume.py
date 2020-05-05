import requests
# def volume(sym):
def volume(arg1, arg2):
    lst = arg1
    #print(lst)
    avg = (sum(lst))/(len(lst))
    if( abs(avg-arg2) > (0.075*avg) ):
        return(1)
        #print(1)
    else:
        return(0)
        #print(0)
