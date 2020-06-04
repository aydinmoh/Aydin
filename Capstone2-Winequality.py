#!/usr/bin/env python
# coding: utf-8

# In[58]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

import seaborn as sns


# In[57]:


#Reading file and show the first 12 rows
Data = pd.read_csv('winequality-white.csv', sep=';')
Data.head(12)


# In[34]:


Data.dtypes


# In[43]:


#Check for empty colums
Data.isnull().any()

Data.info()


# In[19]:


Data.describe()


# In[20]:


# storing unique value in a variable 
Data.nunique()


# In[38]:


#Set the Size of a Figure in Matplotlib
Data.hist(figsize=(10,10));


# In[36]:


#Make estimates of the covariance matrix with Plotting matrix
pd.plotting.scatter_matrix(Data, figsize=(10,10));


# In[37]:


Data.duplicated()


# In[39]:


#Number of columns and missing values 
Data.isnull().sum()


# In[40]:


#Number of Duplication rows in Dataset
sum(Data.duplicated())


# In[61]:


#Data Analysis
display(np.round(Data.describe()))


# In[71]:


n_wines = Data.shape[0]

# Number of wines with quality rating above 6
quality_above_6 = Data.loc[(Data['quality'] > 6)]
n_above_6 = quality_above_6.shape[0]

# Number of wines with quality rating below 5
quality_below_5 = Data.loc[(Data['quality'] < 5)]
n_below_5 = quality_below_5.shape[0]

# Number of wines with quality rating between 5 to 6
quality_between_5 = Data.loc[(Data['quality'] >= 5) & (Data['quality'] <= 6)]
n_between_5 = quality_between_5.shape[0]

# Percentage of wines with quality rating above 6
greater_percent = n_above_6*100/n_wines

# Print the results
print("Total number of wine data: {}".format(n_wines))
print("Wines with rating 7 and above: {}".format(n_above_6))
print("Wines with rating less than 5: {}".format(n_below_5))
print("Wines with rating 5 and 6: {}".format(n_between_5))
print("Percentage of wines with quality 7 and above: {:.2f}%".format(greater_percent))

# Some more additional data analysis
display(np.round(Data.describe()))


# In[66]:


correlation = Data.corr()
# display(correlation)
plt.figure(figsize=(14, 12))
heatmap = sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1,cmap="YlGnBu" )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




