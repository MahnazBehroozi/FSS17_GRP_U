
# coding: utf-8

# In[79]:


import string
import re

# Cleaning the data for deleting the magic characters and deleting comments

File = open("diskFile.txt","r")
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
        
print content
    

File2 = open("clean.txt","w+")
File2.write(content)
File2.close()    
File.close()
print "################################"


# In[80]:


# deleting the rows with falty number of elements per row
Data = []
File = open("clean.txt","r")
for line in File.readlines():
    Data.append(line.split())
print Data[0]
for i in Data:
    #string = map(str,i)
    print i
   # string.split(',')
File.close()

