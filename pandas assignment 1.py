#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd #importing pandas
uber_data=pd.read_csv("Uber_Drives_2016.csv") #reading csv file
uber_data.head()


# In[8]:


uber_data.info() #to know rows and columns
uber_data['CATEGORY*'].unique()
#where category is business


# In[30]:


uber_data['PURPOSE*'].isnull().sum()



# In[9]:


# renaming all columns to uppercase & removing *
uber_data.columns = uber_data.columns.str.replace('*', '', regex=False).str.upper()

uber_data.columns


# In[ ]:





# In[10]:


uber_data[uber_data['CATEGORY'] == 'Business'] 


# In[34]:


uber_data.sort_values(by='MILES', ascending=False).head(5)


# In[11]:


uber_data['PURPOSE'] = uber_data['PURPOSE'].fillna("Not Specified")
uber_data['PURPOSE'].isnull().sum()


# In[13]:


import pandas as pd
uber_data['START_DATE'] = pd.to_datetime(uber_data['START_DATE'], errors='coerce')
uber_data['END_DATE'] = pd.to_datetime(uber_data['END_DATE'], errors='coerce')
uber_data['TRIP_DURATION'] = uber_data['END_DATE'] - uber_data['START_DATE']
uber_data = uber_data.dropna(subset=['TRIP_DURATION'])
print(uber_data[['START_DATE', 'END_DATE', 'TRIP_DURATION']].head())


# In[ ]:





# In[39]:


uber_data.sort_values(by='MILES', ascending=False)



# In[41]:





# In[42]:


p_count = uber_data['PURPOSE'].value_counts()
p_count


# In[43]:


t_start_loc = uber_data['START'].value_counts().head(3)
t_start_loc


# In[ ]:





# In[ ]:





# In[ ]:




