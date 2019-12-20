#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate, train_test_split
df = pd.read_csv('./movies_dataset/ratings.csv')
df = df.drop(columns=['timestamp'])
df.head(5)


# In[ ]:


reader = Reader(rating_scale = (1,5))
data = Dataset.load_from_df(df , reader)
trainset, testset = train_test_split(data, test_size = 0.001)
model = SVD (n_factors = 50)
model.fit(trainset)
model.qi.shape


# In[ ]:


a_user = 1
a_product = 31
result = model.predict(a_user, a_product)
result


# In[ ]:


result.est


# In[ ]:




