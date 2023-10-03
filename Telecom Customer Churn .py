#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(color_codes=True)
pd.set_option('display.max_columns', None)


# In[4]:


df = pd.read_csv('telecom_customer_churn.csv')
df.head()


# In[6]:


# The first step in the Data Preprocessing is to identify the columns to keep and drop if not necessary, 
# here we are dropping Customer ID & 'Zip Code'

df.drop(columns = ['Customer ID', 'Zip Code'], inplace=True)
df.shape


# In[7]:


# Check the number of unique value from all of the object datatype
df.select_dtypes(include='object').nunique()


# In[8]:


# Drop the city column as it has a lot of unique values
df.drop(columns = 'City', inplace = True)
df.shape


# Exploratory Data Analysis

# In[9]:


# Gathering the names of all columns with data type 'object' or categorical columns

cat_var = df.select_dtypes(include = 'object').columns.tolist()

# Add a figure with subplots
num_cols = len(cat_var)
num_rows = (num_cols + 2) // 3
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))
axs =axs.flatten()

# Create a countplot for the top 6 values of each categorial variable using Seaborn
for i, var in enumerate (cat_var):
    top_values = df[var].value_counts().nlargest(6).index
    filtered_df = df[df[var].isin(top_values)]
    sns.countplot(x=var, data=filtered_df, ax=axs[i])
    axs[i].set_title(var)
    axs[i].tick_params(axis='x', rotation=90)
    
# Remove any extra empty Subplots if needed

if num_cols < len(axs):
    for i in range(num_cols, len(axs)):
        fig.delaxes(axs[i])
        
# Adjust spacing between subplots
fig.tight_layout()

# Show_plot
plt.show


# In[10]:


# Get the names of all columns with data type 'int' or 'float'
num_var = df.select_dtypes(include=['int', 'float']).columns.tolist()

# Create a figure with subplots
num_cols = len(num_var)
num_rows = (num_cols + 2) // 3
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))
axs = axs.flatten()

# Create a box plot for each numerical variable using Seaborn
for i, var in enumerate(num_var):
    sns.boxplot(x=df[var], ax=axs[i])
    axs[i].set_title(var)
    
# Remove any extra empty subplots if needed
if num_cols < len(axs):
    for i in range(num_cols, len(axs)):
        fig.delaxes(axs[i])
        
# Adjust spacing between subplots
fig.tight_layout()

# show plot
plt.show()


# In[13]:


# Get the names of all columns with data type 'int'
int_vars = df.select_dtypes(include=['int', 'float']).columns.tolist()

# Create a figure with subplots

num_cols = len(int_vars)

# To make sure there are enough rows for the students
num_rows = (num_cols + 2) // 3
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))
axs = axs.flatten()

# Create a box plot for each integer variable using Seaborn with hue='attrition'
for i, var in enumerate(int_vars):
    sns.boxplot(y=var, x='Customer Status', data=df, ax=axs[i])
    axs[i].set_title(var)
    
# Remove any extra empty subplots if needed
if num_cols < len(axs):
    for i in range(num_cols, len(axs)):
        fig.delaxes(axs[i])
        
# Adjust spacing between subplots
fig.tight_layout()

# Show plot
plt.show()


# In[14]:


# Get the names of all columns with data type 'int'
int_vars = df.select_dtypes(include=['int', 'float']).columns.tolist()

# Create a figure with subplots

num_cols = len(int_vars)

# To make sure there are enough rows for the students
num_rows = (num_cols + 2) // 3
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))
axs = axs.flatten()

# Create a histogram for each integer variable
for i, var in enumerate(int_vars):
    df[var].plot.hist(ax=axs[i])
    axs[i].set_title(var)
    
# Remove any extra empty subplots if needed
if num_cols < len(axs):
    for i in range(num_cols, len(axs)):
        fig.delaxes(axs[i])
        
# Adjust spacing between subplots
fig.tight_layout()

# Show plot
plt.show()


# In[15]:


# Get the names of all columns with data type 'int'
int_vars = df.select_dtypes(include=['int', 'float']).columns.tolist()

# Create a figure with subplots

num_cols = len(int_vars)

# To make sure there are enough rows for the students
num_rows = (num_cols + 2) // 3
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))
axs = axs.flatten()

# Create a histogram for each integer variable with hue='Attrition'
for i, var in enumerate(int_vars):
    sns.histplot(data=df, x=var, hue='Customer Status', kde=True, ax=axs[i])
    axs[i].set_title(var)
    
# Remove any extra empty subplots if needed
if num_cols < len(axs):
    for i in range(num_cols, len(axs)):
        fig.delaxes(axs[i])
        
# Adjust spacing between subplots
fig.tight_layout()

# Show plot
plt.show()


# In[17]:


# Get the names of all columns with data type 'object' (categorical variables)
cat_vars= df.select_dtypes(include=['object']).columns.tolist()

# Exclude 'Attrition' from the list if it exists in cat_vars
if 'Customer Status' in cat_vars:
    cat_vars.remove('Customer Status')
    
# Create a figure with subplots, but only include the required number of subplots
num_cols = len(cat_vars)
# to make sure there are enough rows for the subplots
num_rows = (num_cols +2) // 3 
fig, axs = plt.subplots(nrows=num_rows, ncols=3, figsize=(15, 5*num_rows))
axs = axs.flatten()

# Create a count plot for the top 6 values of each categorical variable
for i, var in enumerate(cat_vars):
    top_values = df[var]. value_counts().nlargest(6).index
    filtered_df = df[df[var].isin(top_values)]
    sns.countplot(x=var, hue='Customer Status', data=filtered_df, ax=axs[i])
    axs[i].set_xticklabels(axs[i].get_xticklabels(), rotation=90)
    
# Remove any remaining blank subplots
for i in range(num_cols, len(axs)):
    fig.delaxes(axs[i])
    
# Adjust spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()


# In[ ]:




