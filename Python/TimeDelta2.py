# The Time Delta, Python, Medium, hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
# Work correctly

import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    date_t1 = datetime.strptime(t1, "%a %d %b %Y %X %z")
    date_t2 = datetime.strptime(t2, "%a %d %b %Y %X %z")
    secounds = abs((date_t1-date_t2).total_seconds())
    return str(int(secounds))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
