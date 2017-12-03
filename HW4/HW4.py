
# coding: utf-8

# In[21]:


import math
import sys
import csv

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
            print ("%d:"%counter, "Range size = %d" %(i-startIndex), ", span = %f" %span(data,startIndex,i), ", lo = %.10f" % min(data[startIndex:i]), ", hi = %.10f" % max(data[startIndex:i]))
            counter = counter + 1
            startIndex = i 
            i = i + int(binSize) 
        else: 
            print ("%d:"%counter, "Range size = %d" %(len(data)-startIndex), ", span = %f" %span(data,startIndex,i), ", lo = %.10f" % min(data[startIndex:i]), ", hi = %.10f" % max(data[startIndex:i]))
            break
            
        
    return binIndeces,data

###############################################################

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
        print ("Label = %d:"%counter, "most = %.10f" %ranges[i][len(ranges[i])-1])
        counter = counter + 1
        
    return ranges


def span(data,startingIndex, endIndex):
    delta = max(data[startingIndex:endIndex]) - min(data[startingIndex:endIndex])
    return delta
####################################################################################

def sortDom(domHolder,Table,features):
    dom = 0
    temp = Table
    for i in range(len(Table.rows)):
         if dominate1(dom,i,Table, features):   
            dom = i
    domHolder.append(dom)        
    del temp[dom]
    sortDom(domHolder,temp,features)

    return domHolder        
            
#####################################################################################            
Table = Tbl()

#FileName = sys.argv[-1]
FileName = 'auto.csv'
row_counter = 0
Num_objectHolder = []
Sym_objectHolder = []
with open(FileName, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #print(reader)
    for row in reader:
        if row_counter == 0:
            print (row)
            for i in range (len(row)):
                txt = row[i][0]
                Table.categories(i,txt)
            for j in range(len(Table.nums)):
                globals()['Num%s' % Table.nums[j]] = num()
                        
            for j in range(len(Table.syms)):
                globals()['Sym%s' % Table.syms[j]] = sym()
            row_counter = 1
        
        else:
            if '?' in row:   # ignoring those rows with missing value
                continue   
                
            else:
                if i in Table.nums:
                    index = Table.nums.index(i)
                    Num_objectHolder.append(globals()['Num%s' % Table.nums[index]].NumUpdate(i, row[i]))

               
                if i in Table.syms:
                    index = Table.syms.index(i)
                    Sym_objectHolder.append(globals()['Sym%s' % Table.syms[index]].SymUpdate(i, row[i]))
            Table.TblUpdate(row)
            

domHolder = []
sortDom(domHolder,Table, Num_objectHolder)
 

