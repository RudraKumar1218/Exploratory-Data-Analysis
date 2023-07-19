#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns


# In[2]:


shop=pd.read_csv('Diwali Sales Data.csv',encoding='unicode_escape')


# In[3]:


shop.head()


# In[4]:


shop.drop(['Status'],axis=1,inplace=True)


# In[5]:


shop.head()


# In[6]:


shop.drop(['unnamed1'],axis=1,inplace=True)


# In[7]:


shop.head()


# In[8]:


shop.isnull().sum()


# In[9]:


shop.dropna(inplace=True)


# In[10]:


shop.isnull().sum()


# In[11]:


shop.info()


# In[12]:


shop['Amount']=shop['Amount'].astype('int')


# In[13]:


shop.columns


# ## Exploratory Data Analysis

# # Gender

# In[14]:


ax = sns.countplot(x = "Gender", data = shop)

for bars in ax.containers:
    ax.bar_label(bars)


# In[15]:


sales_gen = shop.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# From the above graphs we can see that there are more number of female customers than male and the female customers spend more amount on shopping

# ## Age

# In[16]:


ax = sns.countplot(x = "Age Group", data = shop,hue="Gender")

for bars in ax.containers:
    ax.bar_label(bars)


# In[17]:


sales_gen = shop.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_gen)


# From the above graphs we conclude that majority of the buyers are females whose age is between 26-35 years 

# ## Occupation

# In[18]:


ax = sns.countplot(x = "Occupation", data = shop)
sns.set(rc={'figure.figsize':(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)
    


# In[19]:


sales_occ = shop.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)



sns.barplot(x ='Occupation',y= 'Amount' ,data = sales_occ)


# We see that the majority of buyers belong to the IT Sector , Healthcare , Aviation and Banking sector

# ## Product category

# In[20]:


x = sns.countplot(x = "Product_Category", data = shop)

sns.set(rc={'figure.figsize':(50,15)})

for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


#checking the top 10 product categories sold on the basis of amount sold 
sales_productc = shop.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})

sns.barplot(x ='Product_Category',y= 'Amount' ,data = sales_productc)


# From the above graphs we see that although the number of products under Clothing & Apparel are more but higher amount of money was obtained through food
# 
# From this the top selling Product Categories are:
# Food , Clothing & Apparel , Electronics & Gadgets

# In[22]:


sales_productid = shop.groupby(['Product_ID'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})

sns.barplot(x ='Product_ID',y= 'Amount' ,data = sales_productid)


# Highest sales were observed for the product id P00265242

# ## State

# In[23]:


ax = sns.countplot(x = "State", data = shop)
sns.set(rc={'figure.figsize':(25,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[24]:


sales_sta = shop.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(25,5)})

sns.barplot(x ='State',y= 'Amount' ,data = sales_sta)


# In[25]:


sales_staor = shop.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})

sns.barplot(x ='State',y= 'Orders' ,data = sales_staor)


# From the above graphs we see that majority of the buyers were from Uttar Pradesh , Maharashtra , Karnataka

# ## Marital Status

# In[26]:


ax = sns.countplot(data = shop, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(5,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[31]:


sales_marr = shop.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(12,5)})

sns.barplot(data = sales_marr, x = 'Marital_Status',y= 'Amount', hue='Gender')


# Married women constitute the majority of buyers

# ## Conclusion

# Married woman of the age group 26 - 35 working in IT , Healthcare , Aviation , Banking sectors from Uttar Pradesh , Maharashtra , Karnataka are more interested to buy products from Food, Clothing and Electronics category

# In[ ]:




