#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


data = pd.read_csv('mnist_train_100.csv')


# In[8]:


data.head()


# In[9]:


#Extraxting
a=data.iloc[3,1:].values


# In[11]:


a=a.reshape(28,28).astype('uint8')
plt.imshow(a)


# In[12]:


df_x =data.iloc[:,1:]
df_y =data.iloc[:,0]


# In[18]:


x_train, x_test,y_train , y_test = train_test_split(df_x,df_y ,test_size=0.4,random_state=4)


# In[22]:


y_train.head()


# In[24]:


#call rf classifier
rf = RandomForestClassifier(n_estimators=100)


# In[25]:


rf.fit(x_train,y_train)


# In[27]:


pred =rf.predict(x_test)


# In[28]:


pred


# In[30]:


s= y_test.values


c=0
for i in range (len(pred)):
    if pred[i] == s[i]:
        c=c+1;
        


# In[31]:


c


# In[32]:


len(pred)


# In[34]:


24/40


# In[ ]:




