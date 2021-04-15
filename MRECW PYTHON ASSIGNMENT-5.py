#!/usr/bin/env python
# coding: utf-8

# # HOMEWORK ASSIGNMENT

# # Problem 1

# define a series with even values from 100 to 200 in descending order

# In[1]:


import numpy as np
import pandas as pd
np_arr=np.array([i for i in range(100,201)])
even_ctr = list(filter(lambda x: (x%2 == 0) , np_arr))
even_ctr.reverse()
print(even_ctr)
s=pd.Series(even_ctr)
print(s)


# # Problem 2

# assign index to this series starting from 100

# In[2]:


a=[i for i in range(100,151)]
s = pd.Series(even_ctr,index=a)
print(s)


# # Problem 3

# create a dataframe of random values of shape 8*6 . Assign index as numerical values and column names from a to f and using loc and iloc print values of rows 3,4 and columns b and e

# In[3]:


import numpy as np
import pandas as pd
data=pd.DataFrame(np.random.randn(8,6),index='1 2 3 4 5 6 7 8'.split(),columns='a b c d e f'.split())
print(data)


# In[4]:


data.iloc[3:5]


# In[5]:


print(data[['b','e']])


# # Problem 4

# create a multi-index dataframe and 1st index is ["cse","IT"] and second index is 1 to 6 numbers. use 2 columns A,B and assign random values to it 

# In[6]:


arrays = [
          ["cse", "cse", "cse", "cse", "cse", "cse", "IT", "IT","IT","IT","IT","IT"],
          [1, 2, 3, 4, 5, 6,1,2,3,4,5,6],
         ]
tuples = list(zip(*arrays))
print(tuples)


# In[7]:


import numpy as np
import pandas as pd
index = pd.MultiIndex.from_tuples(tuples, names=["A", "B"])
print(index)


# In[8]:


s = pd.Series(np.random.randn(12), index=index)
print(s)


# # Problem 5

# print the row value of number 4 from cse

# In[9]:


s.loc[("cse",4)]


# # Problem 6

# print the row value of 3,5 from IT

# In[10]:


print(s)
s.loc[("IT",3)]


# In[11]:


print(s)
s.loc[("IT",5)]


# In[ ]:




