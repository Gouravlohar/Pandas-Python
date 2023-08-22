#!/usr/bin/env python
# coding: utf-8

# # PANDAS LIBRARY

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


lst={
    "Names":['Gourav','Rahul','Jiten','Adi'],
    "Marks":[50,89,7,6],
    "Grade":['b','a','c','d']
}


# In[3]:


lst


# In[4]:


df=pd.DataFrame(lst)#dataframe will give you a excel tpye sheet
df


# **If You want to convert into csv**

# In[5]:


df.to_csv('first_csv.csv')


# **if you dont want to see index values then**

# In[6]:


df.to_csv('first_csv.csv',index=False)


# **if you want to print head values means first two row**

# In[7]:


df.head(2)


# In[8]:


df.tail(2)


# In[9]:


df.head(3)


# **describe will give you Statistical result from the numeric column**

# In[10]:


df.describe()


# In[11]:


df.max()


# In[12]:


df.min()


# **if you want to read or import csv**

# In[13]:


zomato=pd.read_csv('zomato.csv')


# In[14]:


zomato


# In[15]:


zomato.head(11)


# In[16]:


zomato.head(10)['name']


# In[17]:


zt_rt=zomato.head(11)['rating']


# In[18]:


zt_rt.describe()


# In[20]:


pd.DataFrame(lst)


# for more Information :- https://pandas.pydata.org/docs/user_guide/index.html#user-guide

# In[ ]:




