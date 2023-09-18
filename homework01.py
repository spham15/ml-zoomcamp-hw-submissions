#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
import numpy as np


# In[7]:


pd.__version__


# In[11]:


wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv


# In[75]:


df = pd.read_csv('housing.csv')


# In[65]:


df


# In[42]:


df.shape[1]


# In[43]:


df.isnull().sum()


# In[44]:


df['ocean_proximity'].nunique()


# In[46]:


df[
    df['ocean_proximity'] == 'NEAR BAY'
].median_house_value.mean()


# In[66]:


df['total_bedrooms'].mean()


# In[58]:


mean_total_bedrooms = df['total_bedrooms'].mean()


# In[76]:


df['total_bedrooms'] = df['total_bedrooms'].fillna(value=mean_total_bedrooms)


# In[77]:


df.isnull().sum()


# In[78]:


df['total_bedrooms'].mean()


# In[80]:


df['ocean_proximity'].unique()


# In[84]:


df[
    df['ocean_proximity'] == 'ISLAND'
]


# In[93]:


X = df.loc[df['ocean_proximity'] == 'ISLAND', ['housing_median_age', 'total_rooms', 'total_bedrooms']].to_numpy()
X


# In[94]:


XT = X.T
XT


# In[107]:


XTX = XT.dot(X)
XTX


# In[108]:


XTX_invs = np.linalg.inv(XTX)
XTX_invs


# In[109]:


y = np.array([950, 1300, 800, 1000, 1300])
y


# In[113]:


w = (XTX_invs.dot(XT)).dot(y)


# In[114]:


w[-1]

