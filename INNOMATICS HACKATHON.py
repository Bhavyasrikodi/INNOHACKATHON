#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv("dataset.csv")


# In[3]:


df.shape


# In[4]:


df.describe()


# In[5]:


df.head()


# In[6]:


df.info


# In[7]:


df.isnull().sum()


# In[8]:


from scipy import stats as st
a=st.mode(df['Model'])


# In[9]:


df.fillna(method='bfill', inplace=True)


# In[10]:


df.isnull().sum()


# In[11]:


df.dtypes


# In[12]:


df.duplicated().sum()


# In[13]:


df.corr()


# In[14]:


import seaborn as sns


# In[15]:


sns.heatmap(df.corr())


# In[16]:


import plotly.express as px


# In[17]:


df['Postal Code'].duplicated().sum()


# In[18]:


px.scatter(df,x='Model',y='Model Year')


# In[19]:


px.scatter(df,x='Make',y='Model Year')


# In[20]:


px.scatter(df,x='Make',y='Model')


# In[21]:


px.scatter(df,x='County',y='Electric Range')


# In[22]:


px.scatter(df,x='County',y='Base MSRP')


# In[23]:


px.box(df,x='Model',y='Model Year')


# In[24]:


px.box(df,x='Model',y='Make')


# In[25]:


px.box(df,x='Model',y='Electric Range')


# In[26]:


px.box(df,x='County',y='Base MSRP')


# In[27]:


px.box(df,'Model')


# In[28]:


px.pie(df,'Model Year','Model')


# In[29]:


px.pie(df,'Model Year','Electric Range')


# In[30]:


get_ipython().system('pip install bar-chart-race')


# In[31]:


import bar_chart_race as bcr


# In[32]:


g=df.loc[:, ['County','2020 Census Tract']]
g


# In[34]:


fig=px.choropleth(g,locations='County',color='2020 Census Tract',hover_name='2020 Census Tract',locationmode='country names')
fig.show()


# In[ ]:




