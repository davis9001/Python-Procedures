#!/usr/bin/python

def stamps(pence):
    # Your code here
    if pence >= 5:
        if pence % 5 == 0:
            return pence / 5, 0, 0
        else:
            fives = pence / 5
            remainder = pence % 5
            if remainder % 2 == 0:
                return fives, remainder / 2, 0
            else:
                twos = remainder / 2
                return (fives, twos, remainder % 2)
    elif pence >= 2:
        if pence >= 2:
            if pence % 2 == 0:
                return 0, pence / 2, 0
            else:
                twos = pence / 2
                remainder = pence % 2
                return 0, twos, remainder
    elif pence > 0:
        return (0,0,pence)
    else:
        return (0,0,0)

                


print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps