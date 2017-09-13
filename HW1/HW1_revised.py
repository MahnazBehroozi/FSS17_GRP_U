import math
import sys
import csv
import re
import time

start_time = time.time()

FileName = sys.argv[-1]
File = open(FileName,"r")
content = File.read()
content= re.sub(' ','', content)
index = [] # it holds the index of evey "#" 
dest = [] # It holds the index of the first \n after each "#"

i = 0
while i < len(content):
    if content[i] == "#":
        head, sep, tail = content.partition('#') 
        index.append(i)
        dest.append(content.find("\n", i))
        content = head + tail[content.find("\n", i)-i-1:]
    else:
        i = i + 1  
File2 = open("clean.txt","w+")
File2.write(content)
File2.close()    
File.close()


Data = [] # this holds the data in a list of lists (one list per row)
File = open("clean.txt","r")
for line in File.readlines():
    Data.append(line.split(','))
    
originalLength = len(Data)


for i in range(len(Data)):   # deleting \n from the last element of the list
    Data[i][-1] = Data[i][-1].strip()

DeletedCounter = 0
holder = [] 
for i in range(len(Data)):
    if len(Data[i]) == len(Data[0]):
        holder.append(Data[i])
    else:
        print ('Row number' ,i+1 , 'was faulty because of its length. Has been deleted!')
        DeletedCounter = DeletedCounter + 1
        
Data = holder
#print len(Data)

        
ignore = []
ArrayOfNumObj = []
ArrayOfSymObj = []
#goals = []
#weight = []

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
        #self.cols = []
        self.weight = []
        self.ignore = []          # holds the indeces of the columns that should be ignored
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
        
############################################ 

Table = Tbl()

tempHolder = []
row_counter = 0
for row in Data:
    if row_counter == 0:
        tempHolder.append(Data[row_counter])
        for i in range (len(row)):
            txt = row[i][0]
            Table.categories(i,txt)
        row_counter = 2
            #print Table.x
    else:
        if '?' in row:   # ignoring those rows with missing value
            print('Row number' ,row_counter + DeletedCounter , 'was faulty because it contained missing values. Has been deleted!')
            #DeletedCounter = DeletedCounter + 1
            continue
        flag = 0
        for i in range(len(row)):  
            if i in Table.nums:
                try:
                    float(row[i])
                except ValueError:
                    print('Row number' ,row_counter+DeletedCounter , 'was faulty because it contained a symbolic variable in the place of a numeric variable. Has been deleted!') 
                    #DeletedCounter = DeletedCounter+1
                    flag = 1
                    continue
                
        if flag==0:
            tempHolder.append(Data[row_counter-1])
        row_counter = row_counter + 1

print('#######################################################################################################') 
print(tempHolder)
#print(len(tempHolder))
print('#######################################################################################################') 

print("---Runtime was %s seconds ---" % (time.time() - start_time))
