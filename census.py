#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
census_data=pd.read_csv('census.csv')
census_data.head()


# In[34]:


column_names = ['Age','Education' ,'Marital_Status','Gender','Occupation','Income','Parent_Status','Country','Native','Weeks_Worked'] 
census_data = pd.read_csv("census.csv", names=column_names)
census_data.head()


# In[5]:


# Get the distribution of education levels

education_distribution = census_data['Education'].value_counts()
education_distribution


# In[6]:


import matplotlib.pyplot as plt
education_distribution.plot(kind='bar')
plt.show()


# In[7]:


a=census_data.groupby('Education')['Age'].count()
a.plot(kind='bar')
plt.show()


# In[8]:


a=census_data.groupby(['Education','Gender'])['Age'].count()
a.plot(kind='bar')
plt.show()


# In[10]:


college_dropouts = census_data[census_data['Education'] == 'Somecollegebutnodegree']
college_dropouts.shape[0]


# In[12]:


a=census_data[(census_data['Gender']=='Female') & (census_data['Weeks_Worked']>0)]
a
b=a['Education'].value_counts()
b


# In[13]:


a=census_data.groupby('Education')['Income'].mean().sort_values()
a


# In[14]:


avg_income_by_education = census_data.groupby('Education')['Income'].mean()
avg_income_by_education


# In[15]:


a=avg_income_by_education.get('10thgrade')
b=avg_income_by_education.get('Highschoolgraduate')

print(a)
print(b)
d=[a,b]
labels = ['10th Grade', 'High School Graduate']
plt.pie(d,labels=labels,autopct='%1.1f%%')
plt.show()


# In[16]:


import matplotlib.pyplot as plt

income_values = [991.95, 898.83]  # example values: 10th grade vs High School
labels = ['10th Grade', 'High School Graduate']

plt.figure(figsize=(6,6))
plt.pie(income_values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['orange','green'])
plt.title('Average Income: 10th Grade vs High School Graduate')
plt.show()


# In[17]:


edu_marital_gender = census_data.groupby(['Education', 'Marital_Status', 'Gender']).size()
edu_marital_gender


# In[18]:


edu_marital_gender.plot(kind='bar',figsize=(10,6))
plt.show()


# In[19]:


future_voters = census_data[(census_data['Age'] >= 13) & (census_data['Age'] < 18)]
future_voters.shape[0]


# In[20]:


#No. of Senior Citizen to get added in next 5 years
senior_citizen = census_data[(census_data['Age'] >= 55) & (census_data['Age'] < 60)]
senior_citizen.shape[0]


# In[21]:


#No. of Voters to get added in next X years
X = 5
future_voters = census_data[(census_data['Age'] >= (18 - X)) & (census_data['Age'] < 18)]
future_voters.shape[0]


# In[22]:


#No. of Employable Female Citizens who are Widows or Divorced
employable_females = census_data[
    (census_data['Gender'] == 'Female') &
    ((census_data['Marital_Status'] == 'Widow') | (census_data['Marital_Status'] == 'Divorced')) &
    (census_data['Age'] >= 18) &
    (census_data['Age'] <= 60)
]
employable_females.shape[0]


# In[33]:


#No. of Orphans for each category based on Parents Present
census_data['Parent_Status'].value_counts()


# # Assistant
# This error occurs because the column 'Parents_Status' does not exist in your DataFrame called 'census_data'. The KeyError indicates that Python cannot find this specific key (column name) in your DataFrame.
# 
# Would you like me to provide a corrected version of the code?

# In[39]:


# Calculate gender-wise per capita income
per_capita_income =census_data .groupby('Gender')['Income'].mean().reset_index()

# Rename the column for clarity
per_capita_income.rename(columns={'income': 'Per Capita Income'}, inplace=True)

print(per_capita_income)


# In[40]:


# Per Capita Income for the entire population
per_capita_income = census_data['Income'].mean()
print("Per Capita Income:", per_capita_income)


# In[46]:


# Convert 'salary' column to numeric
census_data['Income'] = pd.to_numeric(census_data['Income'], errors='coerce')

# Group by taxpayer type (parents_status) and sum up salaries
taxpayer_income = census_data.groupby('Parent_Status')['Income'].sum().sort_values(ascending=False)

# Display result
print(" Total Income of Different Types of Tax Payers:\n")
print(taxpayer_income)


# In[47]:


# Calculate Sex Ratio (Male : Female)
males = (census_data['Gender'].str.lower() == 'male').sum()
females = (census_data['Gender'].str.lower() == 'female').sum()
print(f"Sex Ratio (Male : Female) = {males/females:.2f} : 1" if females else "No female data found.")


# In[50]:


education_employment = census_data.groupby(['Education', 'Occupation']).size().reset_index(name='Count')
print("Education Qualification Count based on Employment:\n", education_employment)


# In[51]:


edu_gender_count = census_data.groupby(['Education', 'Gender']).size().reset_index(name='Count')
print("Education Category-wise Gender-wise Count:\n", edu_gender_count)


# In[52]:


widow_females = census_data[(census_data['Gender'] == 'Female') & (census_data['Marital_Status'] == 'Widowed')]
print("Number of Widow Female Candidates:", widow_females.shape[0])


# In[54]:


children_category = census_data.groupby(['Parent_Status', 'Gender']).size().reset_index(name='Count')
print("Number of Children (Parents Category-wise & Gender-wise):\n", children_category)


# In[55]:


age_above_60 = census_data[census_data['Age'] > 60].groupby('Country').size().reset_index(name='Count')
print("Age above 60 Citizens and Non-Citizens:\n", age_above_60)


# In[56]:


employable_widow_divorced = census_data[
    (census_data['Marital_Status'].isin(['Widowed', 'Divorced'])) &
    (census_data['Occupation'] != 'Unemployed')
]
print("Number of Employable Widows and Divorced:", employable_widow_divorced.shape[0])


# In[57]:


total_non_citizens = census_data[census_data['Country'] != 'Citizen'].shape[0]
working_non_citizens = census_data[(census_data['Country'] != 'Citizen') & (census_data['Occupation'] != 'Unemployed')].shape[0]

percent_working = (working_non_citizens / total_non_citizens) * 100
print("Percentage of Non-Citizens Working:", percent_working)


# In[58]:


census_data['Income'] = pd.to_numeric(census_data['Income'], errors='coerce')
non_citizen_income = census_data[census_data['Country'] != 'Citizen']['Income'].sum()
print("Money Generated by Non-Citizens:", non_citizen_income)


# In[59]:


citizens_no_job = census_data[
    (census_data['Country'] == 'Citizen') &
    (census_data['Age'] > 23) &
    (census_data['Occupation'] == 'Unemployed')
]

if not citizens_no_job.empty:
    highest_edu = citizens_no_job['Education'].mode().iloc[0]
    print("Highest Education among Citizens above 23 with no employment:", highest_edu)
else:
    print("No citizens above 23 found with no employment.")


# In[ ]:




