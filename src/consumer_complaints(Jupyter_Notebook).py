
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('complaints.csv')


# In[3]:


df.head()


# In[4]:


df.isnull().sum()


# In[6]:


# Get rid of unnecessary columns
df = df.loc[:, ['Date received', 'Product', 'Company']]


# In[7]:


# Transform date into datetime object
df['Date received'] = pd.to_datetime(df['Date received'])

# and then extract year
df['Date received'] = df['Date received'].map(lambda row: row.year)

# This can be done by doing string split e.g., '2019-02-08'.split('-')[0]
# you won't need datetime object here


# In[8]:


# Make company name case insensitive
# Using str.lower()
df['Company'] = df['Company'].apply(lambda row: row.lower())


# In[9]:


# Add "" for product has comma in its name
def add_quotation(row):
  if ',' in row:
    row = '"' + row + '"'

  return row

df['Product'] = df['Product'].apply(lambda row: add_quotation(row))


# In[10]:


num_complaints = df.groupby(['Product', 'Date received']).size()
num_complaints


# In[11]:


num_companies = df.groupby(['Product', 'Date received'])['Company'].nunique()
num_companies


# In[14]:


num_complaint_company = df.groupby(['Product', 'Date received'])['Company'].value_counts()
num_complaint_company


# In[15]:


percentage = (num_complaint_company) *100/ num_complaints
percentage


# In[16]:


df_output = pd.concat([num_complaints, num_companies], axis=1).reset_index()
df_output


# In[23]:


df_output['highest_percentage'] = 0

for index, group in df.groupby(['Product', 'Date received']):
  product, year = index
  mask = (df_output['Product'] == product) & (df_output['Date received'] == year)
  df_output.loc[mask, 'highest_percentage'] = np.max(round(group['Company'].value_counts()*100 / group['Company'].size))
  
  


# In[24]:


df_output = df_output.rename(columns={0: 'num_complaint', 'Company': 'num_company'})
print(df_output.isnull().sum())
df_output


# In[19]:


df_output.to_csv('output.csv')

