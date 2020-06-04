#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

import seaborn as sns


# In[6]:


#Reading file and show the first 12 rows
Data = pd.read_csv('winequality-white.csv', sep=';')
Data.head(12)


# In[7]:


#Set the Size of a Figure in Matplotlib
Data.hist(figsize=(10,10));


# In[ ]:


.There are 4898 sample of white wine
.There are 12 columns in the dataset
.There are 937 duplicate in white wine and non missing value
.Most wines fall under the average quality
.The quality of wine depends upon a bunch of chemical properties that affect their taste, aroma and flavor


# In[8]:


#Make estimates of the covariance matrix with Plotting matrix
pd.plotting.scatter_matrix(Data, figsize=(10,10));


# In[ ]:


.A lower pH level is an indicator of high acidity.
.Values of pH change with changing fixed acidity levels
.Fixed acidity levels increase, the pH levels drop
.A higher quality is usually associated with low volatile acidity levels
.The good quality wine has more alcohol


# In[9]:


correlation = Data.corr()
# display(correlation)
plt.figure(figsize=(14, 12))
heatmap = sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1,cmap="YlGnBu" )


# In[ ]:




