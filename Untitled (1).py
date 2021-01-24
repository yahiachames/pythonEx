#!/usr/bin/env python
# coding: utf-8

# In[8]:


for x in range(2000,3200):
    if ((x %7) == 0) and ((x%5) != 0):
        print(x)


# In[18]:


def factorial(n):
    
    if(n == 0):
        return 1
    else:
        factorial_value=1
        for x in range(1,n+1):
            factorial_value*=x
        return factorial_value
        

print(factorial(0))


# In[19]:


def dict(n):
    values={}
    for x in range(1,n+1):
        values[x]=x*x
    return values

dict(8)


# In[20]:


def miss_str(str,n):
    return str.replace(str[n],"")

miss_str("kiteen",1)


# In[24]:


import numpy as np


def convert_np_list(array):
    return [list(el) for el in array]


convert_np_list(np.array([[1,2],[1,3]]))


# In[33]:


import numpy as np

def covariance(array1,array2):
    return np.cov([array1,array2])

covariance(np.array([0 ,1,2] ) , np.array([2, 1 ,0]) )


# In[62]:


import numpy as np
import math
def formula(*D):
    C= 50
    H = 30
   
    return [math.floor(math.sqrt(x*C*2/H)) for x in list(D)]

formula( 100,150,180)


# In[ ]:




