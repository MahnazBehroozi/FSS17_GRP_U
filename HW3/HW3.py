import math
import sys
import csv
import random
import numpy as np


def Unsupervised(length):
    data = generator(length)
    n = len(data)
    data = sorted(data)
    epsilon = 0.2*(np.std(data))
    rangeSize = n**0.5
    binSize = math.ceil(rangeSize)
    binIndeces = []
    i = int(binSize)
    startIndex = 0
    while i < n-1:
        while span(data,startIndex,i) < epsilon:
            if i+1 > n-1:
                break
            else:
                i = i + 1
        binIndeces.append(i)
        
        if (i + int(binSize) - 1) < n-1:
            print "Range size = %d" %(i-startIndex), ", span = %f" %span(data,startIndex,i), ", lo = %.10f" % min(data[startIndex:i]), ", hi = %.10f" % max(data[startIndex:i])
            startIndex = i 
            i = i + int(binSize) 
        else: 
            print "Range size = %d" %(len(data)-startIndex), ", span = %f" %span(data,startIndex,i), ", lo = %.10f" % min(data[startIndex:i]), ", hi = %.10f" % max(data[startIndex:i])
            break
            
        
    return binIndeces



def supervised(data):
    pass


def span(data,startingIndex, endIndex):
    delta = max(data[startingIndex:endIndex]) - min(data[startingIndex:endIndex])
    return delta
    
    
def generator(n):
    data = []
    for i in range(n):
        data.append(random.uniform(0, 1))
    
    return data


###########################################################################
Unsup = Unsupervised(50)
