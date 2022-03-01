# find sum of all digits of p
# if sum is single digit, that is the superdigit (x)
# else, repeat from the top
# n = number
# k = times that the number is concatenated (p = nnnn if k = 4)
# find x of n, multiply by k, if >9, find x of that.

import math
import os
# from ossaudiodev import SOUND_MIXER_DIGITAL3
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. STRING n
# 2. INTEGER k
#
def superDigit(n,k):
    digitsList = list(n)
    nDigits = len(digitsList)
    sum = 0
    for i in range (0, nDigits):
        sum += int(digitsList[i])
    x = k * super_digit(sum)
    while (x >=10):
        x = super_digit(x)
    return x
def super_digit(x):
    if (x<10):
        return x
    x_divided = x
    sum = 0
    powerOf10 = int(math.log(x, 10))
    for i in range(0, powerOf10+1):
        sum += x_divided%10
        x_divided = int(x_divided/10)
    return sum

n = "9875"
k = 4
result = superDigit(n, k)
print(result)