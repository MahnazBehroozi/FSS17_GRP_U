import math
import sys
import csv
import numpy as np

ignore = []
ArrayOfNumObj = []
ArrayOfSymObj = []

class Tbl():
    def __init__(self):
        self.rows = []
        self.spec = []
        self.goals = [] 
        self.less = []
        self.more = []
        self.name = []
        self.nums = []
        self.syms = []
        self.cols = []
        self.weight = []
        global ignore           # holds the indeces of the columns that should be ignored
        self.all = []               # holds all the categories 
        self.x = []                 # holds all independent columns
        self.y = []                 # holds all dependent columns
        
        
    def categories(self,i,txt):
        if txt == "$":
            self.nums.append(i)
            self.weight.append(1)
            self.x.append(i)
            self.all.append(i)
            
        elif txt == "<":
            self.nums.append(i)
            self.weight.append(-1)
            self.y.append(i)
            self.all.append(i)
            self.goals.append(i)
            self.less.append(i)
            
        elif txt == ">":
            self.nums.append(i)
            self.weight.append(1)
            self.y.append(i)
            self.all.append(i)
            self.goals.append(i)
            self.more.append(i)
            
        elif txt == "!":
            self.syms.append(i)
            self.weight.append(1)
            self.y.append(i)
            self.all.append(i)
                
        elif txt == "?":
            self.ignore.append(i)
        
        else:
            self.syms.append(i)
            self.weight.append(1)
            self.x.append(i)
            self.all.append(i)
        
        return self.nums, self.syms, self.all, self.x, self.y, self.weight
    
    def TblUpdate(self,row):
        self.items = []
        for i in range(len(row)):
            self.items.append(row[i])
        self.rows.append(self.items)
        
        return self.rows
        
############################################ 

class num():
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.hi = (-math.exp(32))
        self.lo = (math.exp(32)) 
        self.w = 1
        pass
    
    def NumUpdate(self,i,x):
        if i not in ignore:       
            self.n = self.n + 1
            if float(x) < self.lo:
                self.lo = float(x)
            if float(x) > self.hi:
                self.hi = float(x)
            delta = float(x) - self.mu
            self.mu = self.mu + delta / self.n
            self.m2 = self.m2 + delta * (float(x) - self.mu)
            if self.n > 1:
                self.sd = (self.m2 / (self.n - 1))**0.5
        
            return self
    
    def norm(self,i,x):
        if i in ignore:
            return x
        else:
            return (float(x) - self.lo)/(self.hi - self.lo + math.exp(-32))
            
############################################ 

class sym():
    def __init__(self):
        self.n = 0
        self.nk = 0
        self.counts = []
        self.strings = []
        self.most = 0
        self.mode = None
        self._ent = None
        pass
    
    def SymUpdate(self,i,x):
        if i not in ignore:
            self.n = self.n + 1
            self._ent = None
            if str(x) not in self.strings:
                index = len(self.counts)
                self.strings.append(str(x))
                self.counts.append(1)
                
            else:
                index = self.strings.index(str(x))
                self.counts[index] = self.counts[index] + 1 
                
            
            if self.counts[index] > self.most:
                self.most = self.counts[index]
                self.mode = str(x)
        return self
                
    def norm(self,i,x):
        return x
    
################################################

def dominate1(i,j,t, Num):
    e = 2.71828
    n = len(t.goals)
    sum1 = 0
    sum2 = 0
    temp_i = 0
    
    for index in range(len(t.goals)):
        ind = t.goals[index]
        w = t.weight[ind]
        x = Num[ind].norm(ind, t.rows[i][ind])
        y = Num[ind].norm(ind, t.rows[j][ind])
        sum1 = sum1 - e**(w * (float(x)-float(y))/n)
        sum2 = sum2 - e**(w * (float(y)-float(x))/n) 
        if sum1/n < sum2/n:
            temp_i = temp_i + 1       # shows how many times i dominates j
    return sum1/n < sum2/n

################################################
def Unsupervised(TableColumn):
    data = TableColumn
    oldIndices = sorted(range(len(data)), key=lambda k: data[k]) # returns the old index of the elements after sorting 
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
            #print "%d:"%counter, "Range size = %d" %(i-startIndex), ", span = %f" %span(data,startIndex,i), ", lo = %.10f" % min(data[startIndex:i]), ", hi = %.10f" % max(data[startIndex:i])
            counter = counter + 1
            startIndex = i 
            i = i + int(binSize) 
        else: 
            #print "%d:"%counter, "Range size = %d" %(len(data)-startIndex), ", span = %f" %span(data,startIndex,i), ", lo = %.10f" % min(data[startIndex:i]), ", hi = %.10f" % max(data[startIndex:i])
            break
            
        
    return oldIndices, binIndeces,data

###############################################################

#def supervised(data,binIndeces,stdScore):
    #for i in range(len(binIndeces)):
        
####################################################################################

def stdScoreCal(data,binIndeces):
    begin = 0
    score = 0
    for j in range(len(binIndeces)):
        if j == len(binIndeces)-1:
            score = score + (np.std(data[binIndeces[j]:]))*(len(data)-binIndeces[j])
        else:
            score = score + (np.std(data[begin:binIndeces[j]]))*(binIndeces[j]-begin)
            begin = binIndeces[j]
    score = score/len(data)
    return score
####################################################################################
# This function gets a list of lists and returns a column of it (index)
def columnWise(List,index):
    col = []
    for i in range(len(List)):
        col.append(float(List[i][index]))
    return col
#####################################################################################            
Table = Tbl()

#FileName = sys.argv[-1]
FileName = 'auto.csv'
row_counter = 0
Num_objectHolder = []
Sym_objectHolder = []
dataHolder = []
with open(FileName, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        if row_counter == 0:
            for i in range (len(row)):
                txt = row[i][0]
                Table.categories(i,txt)
            for j in range(len(Table.nums)):
                globals()['Num%s' % Table.nums[j]] = num()
            row_counter = 1
        
        else:
            if '?' in row:   # ignoring those rows with missing value
                continue   
                
            else:
                dataHolder.append(row)
                if i in Table.nums:
                    index = Table.nums.index(i)
                    Num_objectHolder.append(globals()['Num%s' % Table.nums[index]].NumUpdate(i, row[i]))

            Table.TblUpdate(row)
            
stdScoreHolder = []
oldIndicesHolder = []
binIndecesHolder = []
#print dataHolder
for i in range(len(Table.nums)-1):
    #columnWise(dataHolder,i)         
    [oldIndices, binIndeces, data] = Unsupervised(columnWise(dataHolder,i+1))
    score = stdScoreCal(data,binIndeces)
    stdScoreHolder.append(score)
    #print binIndeces
    #print oldIndices
print stdScoreHolder
