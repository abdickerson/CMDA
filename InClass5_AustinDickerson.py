Austin Dickerson
In Class Five part One

#1 iPython

#import pandas
import pandas
# pandas.<Tab>

#use ? to find out more about these modules
pandas.stats?
pandas.expanding_mean?
pandas.expanding_max?
pandas.factorize?
pandas.sparse?
#Short cut commands
#Ctrl+l (clears screen)
#up arrow searches through previous command entries
#down arrow also searches through previous command entries
#_i(line number) refers to the input at given line number
#_(line number) refers to the output at given line number
#%run (Program name) runs the given python program file

#magic commands
%reset #deletes all created objects
%run #runs a program
%paste #pastes multiple lines of code from file
%quickref #quick reference card for iPython
%timeit #computes average time of execution for a snippet of code
%hist #input history
%pwd #prints current working directory
%cd #changes working directory to given directory
%ls #lists all the files in your current directory

#copy :
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This uses a for loop to iterate through the values in the_count and print out the string
#"This is the count" along with each value in the list. The %d means the values in the list are integers
for number in the_count:
    print "This is count %d" % number
	
#paste into command line using %paste, this will also run the code
#%xdel deletes a variable, clearing it from anywhere iPython has references to it. The object is also removed from output history
#str.split returns a list of words in the given string, using Sep as the delimiter string
#matplotlib.pylab provides methods to plot sets of data, as well as changing the design of the graph

a = numpy.random.randn(100)
plot(a.cumsum())
#numpy.<Tab>
#numpy.random?
#randn generates normally distributed values
#cumsum returns the cumulative sum of the elements along a given axis
#it takes 21.2 microseconds per loop with 100000 loops
#it takes 184 microseconds per loop with 10000 loops
#it takes 1.61 milliseconds per loop with 1000 loops
#I found this out by using the %timeit function and having 100 randomly generated numbers as the input for this function


# coding: utf-8

# In[7]:

import numpy as np


# In[2]:

data1 = [1, 2, 3, 4, 5]


# In[3]:

data2 = [6, 7, 8, 9, 10]


# In[5]:

array1 = np.array(data1)


# In[6]:

array2 = np.array(data2)


# In[7]:

array1.shape


# In[8]:

array2.shape


# In[9]:

array1.dtype


# In[10]:

array2.dtype


# In[12]:

array1.sum()


# In[13]:

array2.sum()


# In[16]:

array1 * array1


# In[17]:

array2 * array2


# In[18]:

mat = eye(6)


# In[19]:

mat


# In[72]:

mat[2] = 5


# In[73]:

mat


# In[71]:

for i in mat:
    for j in mat:
        if mat[i, j] > 0:
            mat[i, j] = 6


# In[36]:

mat


# In[13]:

arr3 = np.empty((2,3,4), 'int64')


# In[49]:

arr3


# In[42]:

arr3.ndim


# In[43]:

arr3.shape


# In[44]:

arr3.dtype


# In[14]:

arr3[1][2][1][1][0][0] = 5


# In[46]:

arr3


# In[51]:

array = rand(20)


# In[52]:

array


# In[63]:

array.min()


# In[64]:

array.max()


# In[65]:

array.sum()


# In[66]:

array.mean()


# In[67]:

array.std()


# In[10]:

array.where(array[i, j] < 0.5, 0, 1)


# In[6]:

array.sort()


# In[11]:

unique(array)


# coding: utf-8

# In[37]:

import pandas


# In[38]:

import Quandl


# In[39]:

bitstamp = Quandl.get("BCHARTS/BITSTAMPUSD", trim_start="2014-01-01", trim_end="2014-10-30", authtoken="8DAxS1Q5sGp3BcuQByr9")


# In[40]:

bitfinex = Quandl.get("BAVERAGE/USD_BITFINEX", trim_start="2014-04-24", trim_end="2014-10-30", authtoken="8DAxS1Q5sGp3BcuQByr9")


# In[41]:

lakeBTC = Quandl.get("BCHARTS/LAKEUSD", trim_start="2014-03-01", trim_end="2014-10-30", authtoken="8DAxS1Q5sGp3BcuQByr9")


# In[42]:

bitstamp.head()
#The column names are Open, High, Low, Close, Volume (BTC), Volume (Currency) and Weighted Price
#The bitcoin prices increase daily


# In[43]:

bitfinex.head()
#The column names are Ask, Bid, Last, Volume (BTC), Volume (%of Total)
#The bitcoin prices also gradually increase

# In[44]:

lakeBTC.head()
#The column names are Open, High, Low, Close, Volume (BTC), Volume (Currency) and Weighted Price
#The bitcoin prices increase daily

# In[45]:

ind1 = bitstamp.index


# In[46]:

ind2 = bitfinex.index


# In[47]:

ind3 = lakeBTC.index


# In[48]:

ind1


# In[49]:

ind2


# In[50]:

ind3


# In[ ]:

ind1.values
#The type is date values, the dtype is datetime64[ns]

# In[52]:

ind2.values
#The type is date values, the dtype is datetime64[ns]

# In[ ]:

ind3.values
#The type is date values, the dtype is datetime64[ns]

# In[ ]:

bitstamp.columns
#There are 7 columns

# In[26]:

bitfinex.columns
#There are 5 columns

# In[27]:

lakeBTC.columns
#There are 7 columns

# In[ ]:

bitstamp.drop('Volume (BTC)')


# In[ ]:

bitfinex.drop('Volume (BTC)')


# In[ ]:

lakeBTC.drop('Volume (BTC)')
