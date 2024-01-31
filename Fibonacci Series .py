#!/usr/bin/env python
# coding: utf-8

# In[1]:


nterms=int(input("How many terms?"))
n1,n2=0,1
count=0
if nterms<=0:
    print("Please enter a positive integer")
elif nterms==1:
    print("Fibonacci Sequence upto",nterms,":",n1)
else:
    print("Fibonacci Sequence:",end=" ")
    while count<nterms:
        print(n1,end=", ")
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
print(end="...")

