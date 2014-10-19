
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

import matplotlib.pyplot as plt


# In[3]:

project = pd.read_csv('C:\Users\Austin\Desktop\Virginia Tech\CS 3654\CMDA\CollegeOffense.csv')


# In[4]:

project2 = pd.DataFrame(project)


# In[6]:

project2.describe()


# In[7]:

scatter = plt.scatter(project2.YDS, project2.PTS)
plt.title("Scatterplot of Yards and Points")


# In[8]:

scatter2 = plt.scatter(project2.PASS, project2.PTS)
plt.title("Scatterplot of Pass yards and Points")


# In[9]:

scatter2 = plt.scatter(project2.RUSH, project2.PTS)
plt.title("Scatterplot of Rush yards and Points")


# In[10]:

project2.to_pickle('dframe_pickle')


# In[ ]:



