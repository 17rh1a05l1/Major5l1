#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})


# In[3]:


df


# In[4]:


df['A'].fillna(value=df['A'].median(),inplace=True)


# In[5]:


df['B'].fillna(value=df['B'].median(),inplace=True)


# In[6]:


df


# In[27]:


df['A'].fillna(value=df['A'].mode())


# In[28]:


df['B'].fillna(value=df['B'].mode())


# In[29]:


df


# In[ ]:


what is the difference between merging and joining in dataframe


# In[ ]:


Both join and merge can be used to combines two dataframes but the join method combines two dataframes on the basis of their 
indexes whereas the merge method is more versatile and allows us to specify columns beside the index to join on for both 
dataframes.


# In[ ]:


Create a dataframe and add a column, add names in it and use apply function to return names whose length is greater than 5


# In[31]:


names=['Ramya', 'Rama lakshmi', 'Sruthi']


# In[32]:


df['Names'] = names


# In[33]:


df


# In[35]:


df[df['Names'].str.len() > 5]


# In[ ]:


create a numpy array and a dataframe array and concatenate them


# In[40]:


np.ones((3,3))


# In[43]:


data = pd.DataFrame({'X':[1,2,7],
                  'Y':[5,5, 2],
                  'Z':[1,2,3]})


# In[44]:


data


# In[46]:


new_dataframe = pd.concat([
    data,
    pd.DataFrame(np.ones((3,3)), dtype=np.int)
], axis=1, ignore_index=True)


# In[47]:


new_dataframe


# In[ ]:




