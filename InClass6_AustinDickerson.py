
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

import pandas as pd


# In[ ]:

t1 = pd.read_table('ch06\work_tab.txt')


# In[ ]:

t2 = pd.read_csv('ch06/work_comma.csv')


# In[ ]:

t3 = pd.read_table('ch06/stress2_1')


#### df3 = pd.DataFrame(t3)

# In[20]:

import json


# In[21]:

import requests


# In[22]:

t = t1.json()


# In[25]:

table2 = t2.json()


# In[26]:

table3 = t3.json()


# In[27]:

df1 = pd.DataFrame(t, columns = 4)


# In[28]:

df2 = pd.DataFrame(table2, columns = 4)


# In[29]:

df3 = pd.DataFrame(table3, columns = 4)


# In[30]:

df1.to_pickle('dframe_pickle')


# In[ ]:

pd.read_table('dframe_pickle')


# In[32]:

df2.to_pickle('dframe_pickle2')


# In[ ]:

pd.read_table('dframe_pickle2')


# In[34]:

df3.to_pickle('dframe_pickle3')


# In[ ]:

pd.read_table('dframe_pickle3')


# In[37]:

store1 = pd.HDFStore('df1')


# In[38]:

store['df1'] = t1


# In[39]:

store[df1]


# In[40]:

store2 = pd.HDFStore('df2')


# In[42]:

store2['df2'] = t2


# In[43]:

store['df2']


# In[44]:

store3 = pd.HDFStore('df3')


# In[45]:

store3['df3'] = t3


# In[46]:

store['df3']


# In[ ]:


# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np

# <codecell>

import pandas as pd

# <codecell>

project = pd.read_csv('C:\Users\Austin\Desktop\Virginia Tech\CS 3654\CMDA\CollegeOffense.csv')

# <codecell>

project.describe()

# <codecell>

yards1 = [0, 500, 1000, 1500, 2000, 2500]

# <codecell>

yards2 = pd.cut(project.YDS, yards1)

# <codecell>

pd.value_counts(yards2)

# <codecell>

rank = {'(500, 1000]':'low yardage', '(1000, 1500]':'medium yardage', '(1500, 2000]':'large yardage', '(2000, 2500]':'excellent yardage'}

# <codecell>

yards2.map(rank)

# <codecell>

project.rename(columns = {'YDS/G':'Yards per Game', 'YDS':'Yards', 'PTS':'Total Points'})

# <codecell>

sample = np.random.permutation(project.RK)

# <codecell>

train = sample[:62]

# <codecell>

train

# <codecell>

train2 = train[:31]

# <codecell>

train3 = train.take(train2)

# <codecell>

train3.drop_duplicates()

# <codecell>

train3.describe()

# <codecell>



