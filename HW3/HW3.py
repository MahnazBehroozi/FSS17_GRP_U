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
    counter = 1
    while i < n-1:
        while span(data,startIndex,i) < epsilon:
            if i+1 > n-1:
                break
            else:
                i = i + 1
        binIndeces.append(i)
        
        if (i + int(binSize) - 1) < n-1:
            print "%d:"%counter, "Range size = %d" %(i-startIndex), ", span = %f" %span(data,startIndex,i), ", lo = %.10f" % min(data[startIndex:i]), ", hi = %.10f" % max(data[startIndex:i])
            counter = counter + 1
            startIndex = i 
            i = i + int(binSize) 
        else: 
            print "%d:"%counter, "Range size = %d" %(len(data)-startIndex), ", span = %f" %span(data,startIndex,i), ", lo = %.10f" % min(data[startIndex:i]), ", hi = %.10f" % max(data[startIndex:i])
            break
            
        
    return binIndeces,data



def supervised(data,labels):
    ranges = []
    for i in range(len(labels)+1):
        globals()['range%s' % str(i+1)] = []
    number = 2
    i = 0
    for j in range(len(labels)):
    
        while j==0 and data[i] < labels[j]:
            range1.append(data[i])
            i = i + 1
            if i > len(data)-1:
                break
        if j == 0:
            ranges.append(range1)
                
        while i < len(data)-1 and j < len(labels)-1 and labels[j] <= data[i] and data[i] < labels[j+1]:
            globals()['range%s' % str(number)].append(data[i])
            i = i + 1
            if i > len(data)-1:
                    break 
        if number < len(labels) + 1:     
            ranges.append(globals()['range%s' % str(number)])
            number = number + 1
            
        while j == len(labels) - 1 and data[i] >= labels[j]:
            globals()['range%s' % str(number)].append(data[i])
            i = i + 1
            if i > len(data)-1:
                break

    ranges.append(globals()['range%s' % str(number)])
    counter = 1
    for i in range(len(ranges)):
        print "Label = %d:"%counter, "most = %.10f" %ranges[i][len(ranges[i])-1]
        counter = counter + 1
        
    return ranges


def span(data,startingIndex, endIndex):
    delta = max(data[startingIndex:endIndex]) - min(data[startingIndex:endIndex])
    return delta
    
    
def generator(n):
    data = []
    for i in range(n):
        data.append(random.uniform(0, 1))
    
    return data


###########################################################################
print "Unsupervised ranges:\n"
[Unsup, data] = Unsupervised(50)
print "\n Supervised ranges:\n"
sup = supervised(data, [0.2,0.6,0.9])
