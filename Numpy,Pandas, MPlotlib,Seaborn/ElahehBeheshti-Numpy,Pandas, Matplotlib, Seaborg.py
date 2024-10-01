#!/usr/bin/env python
# coding: utf-8

# <h3>Your Choice of Data Processing App
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv('/Users/elahehbeheshti/desktop/Fall2024/heart.csv')

print(df)


# - **age**: Age of the patient
# - **sex**: Gender of the patient (1 = male, 0 = female)
# - **chol**: Serum cholesterol in mg/dl milligrams per deciliter.
# - **fbs**: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
# - **restecg**: Resting electrocardiographic results (values 0, 1, 2)
# - **thalach**: Maximum heart rate achieved
# - **exang**: Exercise-induced angina (1 = yes, 0 = no)
# - **oldpeak**: ST depression induced by exercise relative to rest
# - **slope**: The slope of the peak exercise ST segment
# - **ca**: Number of major vessels (0-3) colored by fluoroscopy
# - **thal**: Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)
# - **target**: Presence of heart disease (1 = disease, 0 = no disease)
# 

# In[4]:


df.describe()


# In[5]:


plt.scatter(df["age"],df["target"])


# In[6]:


plt.scatter(df["sex"],df["target"])


# In[7]:


plt.scatter(df["chol"],df["target"])


# In[8]:


plt.scatter(df["fbs"],df["target"])


# In[9]:


plt.scatter(df["restecg"],df["target"])


# In[10]:


plt.scatter(df["thalach"],df["target"])


# In[11]:


plt.scatter(df["exang"],df["target"])


# In[12]:


plt.scatter(df["oldpeak"],df["target"])


# In[13]:


plt.scatter(df["slope"],df["target"])


# In[14]:


##oldpeak< 5
###thalach >80
####chol <500


# In[15]:


print("\n The total number of missing values for each column:\n\n", df.isnull().sum())


# In[16]:


for i in range(len(df.index)):
    print(("Total NaN in row", i + 1, ":"), df.iloc[i].isnull().sum())


# In[17]:


df1=df.drop("slope", axis=1)
df1


# In[18]:


df1.dropna(inplace=True)
df1.describe()


# In[19]:


print("\n The total number of missing values for each column:\n\n", df1.isnull().sum())


# In[20]:


##Type one error = Missing values done!
##Type 2 error = Noise


# In[21]:


##oldpeak< 5
###thalach >80
####chol <500


# In[22]:


High = df1["chol"].nlargest(3)
High


# In[23]:


###we will drop 564


# In[24]:


df2=df1[df1["chol"]<564]
df2


# In[25]:


small=df1["thalach"].nsmallest(3)
small


# In[26]:


df3=df2[df2["thalach"]>71]
df3


# In[27]:


High2= df3["oldpeak"].nlargest(3)
High2


# In[28]:


Df = df3[df3["oldpeak"]<5.6]
Df


# In[29]:


#Now we get ride of missing values and noises, so we take some plots to see 


# In[30]:


plt.scatter(df["chol"], df["target"])


# In[31]:


plt.scatter(Df["chol"], Df["target"])


# In[32]:


plt.scatter(df["oldpeak"],df["target"])


# In[33]:


plt.scatter(Df["oldpeak"],Df["target"])


# In[34]:


plt.scatter(df["thalach"],df["target"])


# In[35]:


plt.scatter(Df["thalach"],Df["target"])


# In[36]:


# Plot histograms for continuous variables
Df.hist(column=["age", "chol", "thalach", "oldpeak"], bins=20, figsize=(10, 8))
plt.show()


# In[37]:


##b. Correlation Matrix

##This will help you see how the features are correlated with each other and the target.

import seaborn as sns

# Correlation matrix
plt.figure(figsize=(10, 8))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix of Features")
plt.show()


# In[38]:


# Boxplot to visualize outliers
plt.figure(figsize=(8, 5))
sns.boxplot(Df["chol"])
plt.title("Boxplot of Cholesterol")
plt.show()


# Loaded the Dataset
# 
# 
# Explored Dataset Features
# 
# 
# Identified Missing Values
# 
# 
# Handled Missing Values
# 
# 
# Identified Noise in the Data
# 
# 
# Visualized Data
# 
# 
# Evaluated Dataset After Cleaning
# 
# 
# Summarized Key Insights
# 
# 
# The next step would be to use this cleaned dataset to train a machine learning model that can predict the likelihood of heart disease based on these features.
# 
# 
# THE END!

# In[ ]:




