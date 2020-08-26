#!/usr/bin/env python
# coding: utf-8

# # Live Project- finding the best data segmentation model for given problem statement
### version 4- after performing prediction usig multiple models such as logistic regressor, decision tree,

# ### Importing the libraries

import pandas as pd
import numpy as np
import sys
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score


# ### Taking input(dataset) from command line

# In[14]:


data= pd.read_csv(sys.argv[1])
print(data)


# ### Data Preprocessing
# Removing columns with null values

# In[26]:


data.drop(['Certifications/Achievement/ Research papers', 'Link to updated Resume (Google/ One Drive link preferred)', 'link to Linkedin profile'], axis=1)


#  Encoding categorical values using label encoding

# In[92]:


data['newLabel'] = LabelEncoder().fit_transform(data['Label'])
data['newYear'] = LabelEncoder().fit_transform(data['Which-year are you studying in?'])
data['newCGPA'] = LabelEncoder().fit_transform(data['CGPA/ percentage'])
data['newLang'] = LabelEncoder().fit_transform(data['Programming Language Known other than Java (one major)'])
data['newOOP']= LabelEncoder().fit_transform(data['Have you studied OOP Concepts'])
data['newInterest'] = LabelEncoder().fit_transform(data['Areas of interest'])
data['newDB'] = LabelEncoder().fit_transform(data['Have you worked on MySQL or Oracle database'])
data['newJava'] = LabelEncoder().fit_transform(data['Have you worked core Java'])
data['newWritten'] = LabelEncoder().fit_transform(data['Rate your written communication skills [1-10]'])
data['newVerbal'] = LabelEncoder().fit_transform(data['Rate your verbal communication skills [1-10]'])

encoded_labels= ['newYear','newCGPA','newLang','newInterest','newDB','newJava','newOOP','newWritten','newVerbal']
X = data[encoded_labels]
Y = data['newLabel']


# ### Splitting training and testing data

# In[93]:


X_train,X_test,Y_train, Y_test = train_test_split(X,Y, test_size=0.25, random_state=30)


# Various Binary classification models were implemented to check for the most appropriate model, and the one I have chosen based on the F1 score metric is the Random Forest Classifier


final_model_rfc=RandomForestClassifier(n_estimators=3)

final_model_rfc.fit(X_train, Y_train)


# In[96]:


Predicted_Y= final_model_rfc.predict(X_test)


# The metric F1 score is used to indicate the accuracy and precision of the model's prediction

F1_Score= f1_score(Y_test, Predicted_Y)

print(F1_Score)
