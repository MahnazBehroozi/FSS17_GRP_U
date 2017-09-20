
# coding: utf-8

# In[113]:


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

Table = Tbl()

FileName = sys.argv[-1]
#FileName = 'auto.csv'
row_counter = 0
Num_objectHolder = []
Sym_objectHolder = []
with open(FileName, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        if row_counter == 0:
            print row
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

FirstDomHolder = [] 
dom = 0

for domNumber in range(5):
    iterate = len(Table.rows)
    i = 0
    j = 1
    while iterate > 1 and i<len(Table.rows) and j<len(Table.rows):
        if j in FirstDomHolder:
            j = j + 1
            iterate = iterate - 1
        elif i in FirstDomHolder:
            i = i + 1
            dom = i
            
        
        if dominate1(i,j,Table, Num_objectHolder):
            dom = i
            j = j + 1
        else:
            iterate = iterate - j
            i = j
            j = i + 1
             
    FirstDomHolder.append(dom)
    
    
LastDomHolder = [] 
dom = 0

for domNumber in range(5):
    iterate = len(Table.rows)
    i = 0
    j = 1
    while iterate > 1 and i<len(Table.rows) and j<len(Table.rows):
        if j in LastDomHolder:
            j = j + 1
            iterate = iterate - 1
        elif i in LastDomHolder:
            i = i + 1
            dom = i
            
        if not dominate1(i,j,Table, Num_objectHolder):
            dom = i
            j = j + 1
        else:
            iterate = iterate - j
            i = j
            j = i + 1
             
    LastDomHolder.append(dom)

print "\n"   
#print "Top 5 dominant records:\n"
for i in FirstDomHolder:
    print Table.rows[i]
print "\n\n"

#print "Bottom 5 dominate records:"
j = len(LastDomHolder) - 1
for i in LastDomHolder:
    print Table.rows[LastDomHolder[j]]
    j = j - 1
