#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import the dataset using pandas and perform operations on it


# In[1]:


import pandas as pd
data=pd.read_csv("IRIS.csv")
data


# In[ ]:


# perform some operations in dataset


# In[4]:


max=data['sepal_width'].max()   # to known maximum value in sepal_width
max


# In[5]:


min=data['petal_length'].min()  # to known minimum value in petal_width
min


# In[6]:


mean=data['petal_width'].mean()   # to known mean of the petal_width
mean


# In[7]:


std=data['sepal_length'].std()   #to known the standard deviation of sepal_length
std


# In[8]:


var=data['petal_width'].var()  # to known variance of petal_width
var


# In[9]:


median=data['sepal_width'].median()  #to known the median value of sepal_width
median


# In[10]:


mode=data['sepal_length'].mode()
mode


# In[15]:


data.iloc[[9]]   # to known the particular index


# In[16]:


data.iloc[9]


# In[17]:


data.info()    #The info() method of DataFrame displays information such as the number of rows and columns, total memory usage, the data type of each column, and the count of non-NaN elements.


# In[18]:


data.describe()  #perform some basic opertion like mean,maximum,minimum,std,variance


# In[21]:


data.size  # to known the total size of the dataset like row * column


# In[22]:


len(data.columns) #to known the columns in dataset


# In[25]:


len(data)  # to known the rows in given dataset


# In[26]:


data.head()


# In[27]:


data.tail()

