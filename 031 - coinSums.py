"""
Coin Sums: How many different ways can £2 be made using any number of coins,
when the coins have denominations 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2
(200p)?
"""
import math

denominations = [1, 2, 5, 10, 20, 50, 100, 200]

## very inefficient! Find a better algorithm!
def numWays(money):
    res = []
    for a in range(math.ceil(money/1) + 1):
        v1 = 1*a
        for b in range(math.ceil((money-v1)/2) + 1):
            v2 = 2*b
            for c in range(math.ceil((money-v1-v2)/5) + 1):
                v5 = 5*c
                for d in range(math.ceil((money-v1-v2-v5)/10) + 1):
                    v10 = 10*d
                    for e in range(math.ceil((money-v1-v2-v5-v10)/20) + 1):
                        v20 = 20*e
                        for f in range(math.ceil((money-v1-v2-v5-v10-v20)/50) + 1):
                            v50 = 50*f
                            for g in range(math.ceil((money-v1-v2-v5-v10-v20-v50)/100) + 1):
                                v100 = 100*g
                                for h in range(math.ceil((money-a-v2-v5-v10-v20-v50-v100)/200) + 1):
                                    v200 = 200*h
                                    tmp = v1+v2+v5+v10+v20+v50+v100+v200
                                    if tmp == money:
                                        tmp_d = {1:a,2:b,5:c,10:d,20:e,50:f,100:g,200:h}
                                        # print(tmp_d)
                                        if tmp_d not in res:
                                            res.append(tmp_d)
    return len(res)
