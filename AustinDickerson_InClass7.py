
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

import matplotlib.pyplot as plt


# In[3]:

project = pd.read_csv('C:\Users\Austin\Desktop\Virginia Tech\CS 3654\CMDA\CollegeOffense.csv')


# In[4]:

project.head()


# In[5]:

hist = project.YDS.hist(bins = 7)
plt.title("Histogram")


# In[6]:

density = project.YDS.plot(kind = 'kde')
plt.title("Density Plot")


# In[7]:

bar = project.YDS.plot(kind = 'bar')
plt.title("Bar Graph")


# In[8]:

bar2 = project.div(project.sum(1).astype(float), axis = 1)


# In[ ]:

bar3 = bar2.plot(kind = 'bar', stacked = TRUE)
plt.title("Side by side bar graph")


# In[9]:

scatter = plt.scatter(project.YDS, project.RUSH)
plt.title("Scatterplot")


# In[10]:

hist.savefig('hist.png', dpi=400, bbox_inches='tight')
density.savefig('density.png', dpi=400, bbox_inches='tight')
bar.savefig('bar.png', dpi=400, bbox_inches='tight')


# In[11]:

bar3.savefig('bar3.png', dpi=400, bbox_inches='tight')


# In[12]:

scatter.savefig('scatter.png', dpi=400, bbox_inches='tight')


# In[ ]:




# coding: utf-8

# In[1]:

import pandas as pd


# In[3]:

import scipy as sp


# In[4]:

import numpy as np


# In[7]:

import matplotlib.pyplot as plt


# In[8]:

import sklearn as sk


# In[2]:

medical = pd.read_csv('Downloads\Medical.csv')


# In[9]:

medical2 = array(medical[['Age', 'HgA1C']])


# In[12]:

literacy = array(medical.A_Literacy_Category)


# In[14]:

from sklearn.cross_validation import train_test_split
medical2_train, medical2_test, literacy_train, literacy_test = train_test_split(medical2, literacy, test_size=0.25 random_state=33)


# In[18]:

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(medical2_train)
medical2_train = scaler.transform(medical2_train)
medical_test = scaler.transform(medical2_test)


# In[19]:

from sklearn.linear_model import SGDClassifier
clf = SGDClassifier()
clf.fit(medical2_train, literacy_train)


# In[20]:

clf.coef_


# In[21]:

from sklearn import metrics
literacy_train_pred = clf.predict(medical2_train)
metrics.accuracy_score(literacy_train, literacy_train_pred)


# In[22]:

from sklearn import metrics
literacy_test_pred = clf.predict(medical2_test)
metrics.accuracy_score(literacy_ttest, literacy_test_pred)


# In[23]:
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[2]:

import sklearn as sk
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt


## Principal Components Analysis

#### Dimensionality Reduction and Visualization

####### #Get the digits data

# In[3]:

from sklearn.datasets import load_digits
digits = load_digits()


####### #What does the digits dataset contain?

# In[4]:

print digits.keys()


####### #Each row of data in X_digits corresponds to one of the following digits:

# In[5]:

digits.target_names


# In[6]:

X_digits, y_digits = digits.data, digits.target


####### #What does the X matrix look like?

# In[7]:

X_digits.shape


####### #Get the first 10 principal components of the X_digits matrix

# In[8]:

from sklearn.decomposition import PCA

estimator = PCA(n_components=10)
X_pca = estimator.fit_transform(X_digits)


####### #What does the PCA matrix looks like

# In[9]:

X_pca.shape


# In[10]:

X_pca


####### #Visualize our data using the first two principal components in a scatterplot

# In[13]:

colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
for i in xrange(len(colors)):
    px = X_pca[:, 0][y_digits == i]
    py = X_pca[:, 1][y_digits == i]
    plt.scatter(px, py, c=colors[i])
plt.legend(digits.target_names)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')


# In[12]:

#Digits 0, 6, and 4 are the easiest to separate because they are mostly separated from the other 7.
#Digits 8, 2, 7, and 5 are more confounded because they are jumbled together on the scatterplot


# In[14]:

colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
for i in xrange(len(colors)):
    px = X_pca[:, 8][y_digits == i]
    py = X_pca[:, 9][y_digits == i]
    plt.scatter(px, py, c=colors[i])
plt.legend(digits.target_names)
plt.xlabel('Eighth Principal Component')
plt.ylabel('Ninth Principal Component')


# In[15]:

#This scatterplot is more confusing to distinguish between the ten values, they are more clustered together than in the other scatterplot


# In[ ]:





literacy_pred = clf.predict(medical2_test)
print metrics.accuracy_score(literacy_test, literacy_pred)


# In[24]:

medical2_pred = clf.predict(medical2_train)
print metrics.accuracy_score(literacy_train, medical2_pred)


# In[25]:

metrics.confusion_matrix(literacy_test, literacy_pred)


# In[ ]:



