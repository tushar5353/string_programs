import sys
import math
from collections import defaultdict


berth = int(sys.argv[1])

block = defaultdict(list)



def get_seat_info(berth):
    for i in range(1,73):
        block[math.ceil(i/8)].append(i)
    index = block[math.ceil(berth/8)].index(berth)
    if index == 0 or index == 3:
        return "LB"
    if index == 1 or index == 4:
        return "MB"
    if index == 2 or index == 5:
        return "UB"
    if index == 6:
        return "SL"
    if index == 7:
        return "SU"


print(get_seat_info(berth))
