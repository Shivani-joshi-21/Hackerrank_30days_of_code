import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = bin(n).replace("0b", "")
    res = list(map(int, str(binary))) 
    count=0
    temp=0
    for i in range(len(res)):
        if(res[i]==0):
            count=0
        else:
            count+=1
            if(count>temp):
                temp=count
    print (temp)
