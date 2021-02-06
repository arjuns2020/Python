

ALL_PRICES = [
    9961,
    6219,
    6848,
    9007,
    4935,
    4825,
    2357,
    2604,
    1216,
    2796,
    9726,
    6759,
    4620,
    3609,
    1198
]

def compute_mean(prices):
    n = len(prices)
    #case 1 - even nos
    if n%2==0:
        m1 = sorted(prices)[n//2]
        m2 = sorted(prices)[n//2-1]
        median = (m1+m2)/2
        return median
    else:
        return prices[n//2]
        

    


[compute_mean(ALL_PRICES)]
