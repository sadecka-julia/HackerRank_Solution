# The Time Delta, Python, Medium, hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
# DO NOT WORKING CORRECTLY
# after that I read about datetime and strptime

# Input
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

# Output
# 25200
# 88200

#!/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    secounds_t1 = secounds(t1)
    secounds_t2 = secounds(t2)
    return abs(secounds_t1-secounds_t2)
    


def days_in_year(day, month, year):
    days_in_month = 0
    month_number = datetime.strptime(month, "%b").month
    for i in range(1, month_number):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            days_in_month += 31
        elif i == 2 and int(year % 4 == 0):
            days_in_month += 28
        elif i == 2 and int(year % 4 != 0):
            days_in_month += 29
        else:
            days_in_month += 30
    days_in_month += (day-1)
    return days_in_month

def secounds(t):
    date_array = t.split()
    hour_array = date_array[4].split(':')
    time_zone = int(date_array[5][1:3])*3600 + int(date_array[5][3:5])*60
    if int(date_array[5]) > 0:
        time_zone = time_zone*(-1)

    days = days_in_year(int(date_array[1]), date_array[2], int(date_array[3]))     
    amount_secounds = int(date_array[3])*31536000 + (days)*86400
    amount_secounds += int(hour_array[0])*3600 + int(hour_array[1])*60 + int(hour_array[2])
    amount_secounds += time_zone
    return amount_secounds



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())


    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)

        # fptr.write(delta + '\n')

    # fptr.close()