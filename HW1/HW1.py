import string
import re
import time
import numpy as np

start_time = time.time()

# Cleaning the data for deleting the magic characters and deleting comments

#File = open("diskFile.txt","r")
File = open("POM3A.txt","r")
content = File.read()
content= re.sub('[~@!$%^&*(){}<>]','', content)
content= re.sub(' ','', content)
#print content
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
#print "################################"

# deleting the rows with faulty number of elements per row

Data = [] # this holds the data in a list of lists (one list per row)
File = open("clean.txt","r")
for line in File.readlines():
    Data.append(line.split(','))
    
for i in range(len(Data)):   # deleting \n from the last element of the list
    Data[i][-1] = Data[i][-1].strip()

holder = [] 
for i in range(len(Data)):
    if len(Data[i]) == len(Data[0]):
        holder.append(Data[i])
    else:
        print 'Row number' ,i , 'was faulty and has been deleted!'
#print holder
Data = holder

# deleting the column with "?" 

sub = "?"
i = 0
junkColumn = []
while i < len(Data[0]):
    if any(sub in string for string in Data[0][i]):     
        junkColumn.append(i) #the indeces of the columns that has to be deleted
    i = i+1
for i in range(len(junkColumn)):
    for row in Data:
        del row[junkColumn[i]]
#print Data

outarr = np.vstack(Data)
print outarr

File3 = open("ProcessedData.txt","w+")
for i in range(len(Data)):
    for j in range(len(Data[0])):
        if j < len(Data[0])-1:
            File3.write(str(Data[i][j]) + ',')
        else:
            File3.write(str(Data[i][j]) + '\n')
    
File3.close()  
File.close()

# Runtime report

print("---Runtime was %s seconds ---" % (time.time() - start_time))

