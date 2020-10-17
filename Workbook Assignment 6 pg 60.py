#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


df = df.sort_values(by = 'age', ascending= 0)
df.head()


# In[15]:


df = df.sort_values(by =['fname','age','grade'], ascending=[True, True, True])
df.head()


# In[ ]:





# In[ ]:




