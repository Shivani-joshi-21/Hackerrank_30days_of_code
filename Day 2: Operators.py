#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent/100
    tax= meal_cost *tax_percent/100
    total_cost = tip + tax + meal_cost

    return int(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(raw_input())

    tip_percent = int(raw_input())

    tax_percent = int(raw_input())

    a=solve(meal_cost, tip_percent, tax_percent)
    print a
