from math import floor
from decimal import *

def main(num):
    max = (0,0)
    sequence_length = 0
    for i in range(2,num):
        if sequence_length >= i:
            break
        found_remainders = []
        value = 1
        position = 0

        while found_remainders[value] == 0 and value != 0:
            found_remainders[value] = position
            value *= 10
            value %= i
            position += 1
        
        if position - found_remainders[value] > sequence_length:
            sequence_length = i
            max = (i,sequence_length)
        
    print(max)
    return None

main(1000)