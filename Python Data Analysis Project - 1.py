#!/usr/bin/env python
# coding: utf-8

# # Working on Real Time Project with Python 

# # Weather Dataset
A big dataset has daily weather info from lots of major cities. At first, it only had capitals, but now it covers more cities and even has hourly data. There are about 1250 cities included. Some places have weather records going way back to January 2, 1833. This helps users see how weather patterns have changed over a long time.
# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[2]:


df = pd.read_csv(r'C:\Users\LENOVO\Desktop\Self Prep\Python DA Project-1\weatherHistory.csv')


# In[3]:


df


# # Analyzing DataFrames

# - .head() - Shows first N rows in the data. By default N=5

# In[4]:


df.head()


# - .shape -
# Shows total no of rows & columns in Dataframe

# In[5]:


df.shape


# - .index - provide index of dataframe
# 

# In[6]:


df.index


# - .columns - shows name of each column

# In[7]:


df.columns


# - .dtypes - Shows data-type of each column

# In[8]:


df.dtypes


# - .unique() - shows unique values in column. Apply only at single column

# In[9]:


df['Summary'].unique()


# - .nunique() - Shows total count of unique values. Apply on single column or whole DataFrame
# 

# In[10]:


df.nunique()


# - .count() - shows total no of non-null values in each column. Can be applied on single column as well as whole dataframe

# In[11]:


df.count()


# - .value_counts - shows the unique values with their count. Applied on single column only

# In[12]:


df.value_counts


# - .info - Provides basic information about the dataframe

# In[13]:


df.info


# # Finding the unique wind speed in the dataset

# In[14]:


df.head()


# - .nunique() - Shows total no of uniques values. Can be applied on sinlge column or whole Dataframe

# In[15]:


df.nunique()


# In[16]:


df['Wind Speed (km/h)'].nunique()


# - .unique() - Shows unique values in columns. Work on single column only

# In[17]:


df['Wind Speed (km/h)'].unique()


# # Analyzing where the weather is rainy

# In[18]:


df.head(2)


# - Vaule_count() - shows no of common counts (yes / no / neutral)

# In[19]:


df['Precip Type'].value_counts()


# - Filtering - Select specific rows based on given conditions

# In[20]:


df[df['Precip Type'] == 'rain']


# - Groupby () - Split DataFrame based on specified column

# In[21]:


df.groupby('Summary').get_group('Partly Cloudy')


# # Finding the Wind Speed when it is exactly 5.8765

# In[22]:


df[df['Wind Speed (km/h)'] == 5.8765]


# # Finding Null Values in the Data

# In[23]:


df.isna()


# In[24]:


df.isnull()


# In[25]:


df.notnull().sum()


# # Renaming column name "Summary" to "Weather" in dataframe

# - Temporary Rename

# In[26]:


df.rename(columns = {'Summary' : 'Weather'})


# - Permanently Rename

# In[27]:


df.rename(columns = {'Summary' : 'Weather'},inplace = True)


# In[28]:


df.head(1)


# # Analyzing Mean Visibility

# In[29]:


df['Visibility (km)'].mean()


# # Analyzing Standard Deviation of 'Pressure' in Data

# In[30]:


df['Pressure (millibars)'].std()


# # Finding Variance of "Humidity"

# In[31]:


df['Humidity'].var()


# # Analyzing all the instances when 'Dry' was Recorded

# In[32]:


df['Weather'].value_counts()


# In[33]:


df[df['Weather'] == 'Dry']


# - str.contains -  filters rows in the DataFrame where the values in a particular column contain the specified substring.

# In[34]:


df[df['Weather'].str.contains('Dry')]


# # Finding mean value of each column against each 'Weather'

# In[35]:


df.groupby('Weather').mean()


# # Analyzing Min & Max value of eacch column against each 'Weather'

# In[36]:


df.groupby('Weather').min()


# In[37]:


df.groupby('Weather').max()


# # Finding all the records when Weather Condition is Fog

# In[38]:


df[df['Weather'] == 'Foggy']


# # Analyzing the instance when Weather is Foggy or Visibility is Above 0.7245

# In[39]:


df[(df['Weather'] == 'Foggy') | df['Visibility (km)'] > 0.7245		]


# # Finding all instances when -

# # A. Whether is Dry & HUmidity is above 0.26

# In[40]:


df.head(1)


# In[41]:


df[(df['Weather'] == 'Dry') | df['Humidity'] > 0.26]

