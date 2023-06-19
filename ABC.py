#!/usr/bin/env python
# coding: utf-8

# In[2]:


def checkA(*args):
    
    for x in args:
        if not (isinstance(x,(int,float))):
            return False 
    return True 
def addA(*args):
    s = 0
    for x in args:
        s += x
    return s 

myName = "Python"
            


# In[ ]:




