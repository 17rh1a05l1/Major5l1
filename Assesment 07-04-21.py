#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
import numpy as np
rand_num=np.random.normal(0,1,15)
print("15 random numbers from a standard normal distribution:")
print(rand_num)


# In[2]:


#Create an array of 20 linearly spaced points between 0 and 1
import numpy as np
np.linspace(1,10)


# In[4]:


#declare a numpy array of values from 1 to 100 and make it into a 10*10 matrix. 
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr)


# In[5]:


#using the previously defined matrix print rows 1,5,6
#	using the previously defined matrix print elemnts from 3rd row  to 10th row
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[1])
print(arr[5])
print(arr[6])
    


# In[7]:


#using the previously defined matrix print all elemtnts from 4th column to 8th column
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[4:9])


# In[9]:


#using the same matrix print values from 3rd row 2nd coumn to 5th row 8th column
import numpy as np
arr=np.arange(1,101).reshape(10,10)
print(arr[3:6,2:9])


# In[10]:


#write a code to generate a 1000 random numbers each in the range(0,1) such that the count of all random points like are almost same .
from random import seed
from random import randint
seed(1)
for _ in range(10):
    value=randint(0,10)
    print(value)


# In[11]:


#write the commands to get standard deviation, mean ,mode,median for a given vector
import statistics


# In[14]:


statistics.mean([1,2,3,4,5,6])


# In[15]:


statistics.median([3,4,5,6])


# In[20]:


statistics.mode([7,3,3,5])


# In[ ]:




