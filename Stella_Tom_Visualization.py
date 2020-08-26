#!/usr/bin/env python
# coding: utf-8

# # Visualisation Model to draw insights from the given dataset

# In[11]:


import pandas as pd
import numpy as np
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# In[12]:


data = pd.read_csv(sys.argv[1])
# data


# Data preprocessing

# In[13]:


data.drop(['Certifications/Achievement/ Research papers', 'Link to updated Resume (Google/ One Drive link preferred)', 'link to Linkedin profile'], axis=1)


# Using PdfPages will ensure the ouput plots are tranformed into a pdf document of all the plots combined

# In[16]:


with PdfPages(final_visualisation_output.pdf) as pdf :


# Plots:-
#
# a) The number of students applied to different technologies.
# the 'Area of interest' field is used to plot the result of(a)
#

# In[14]:


plt.figure(figsize=(12,8))
data['Areas of interest'].value_counts().plot(kind='barh', color='green')
plt.title('Number of students applied for different technologies')
plt.ylabel('Technologies')
# pdf.savefig()
# plt.savefig('fig1.png')


# In[73]:


plt.close()
# plt.clf()


# b)The number of students applied for Data Science who knew ‘’Python” and who didn’t.

# In[74]:


df = data.filter(['Areas of interest','Programming Language Known other than Java (one major)'], axis=1)
df=df.loc[(data['Areas of interest']=='Data Science ')]
df['python']=np.where(df['Programming Language Known other than Java (one major)']=='Python','Know python','Do not know python')
df


# In[75]:


labels= 'Do not know python' , 'know python'
colors= 'orange','yellow'
fig= plt.pie(df['python'].value_counts(),labels=labels,colors=colors,autopct='%1.1f%%')
plt.title('students who applied for data science that :')
pdf.savefig()


# In[76]:


plt.close()
# plt.clf()


# c) The different ways students learned about this program

# In[77]:


plt.figure(figsize=(12,8))
data['How Did You Hear About This Internship?'].value_counts().plot(kind='barh', color='purple')
plt.title('Ways students learned about this internship')
plt.ylabel(' ')
pdf.savefig()


# In[78]:


plt.close()


# d) Students who are in the fourth year and have a CGPA greater than 8.0

# In[79]:


df = data.filter(['Which-year are you studying in?','CGPA/ percentage'], axis=1)
df=df.loc[(data['Which-year are you studying in?']=='Fourth-year')]
df['cgpa']=np.where(df['CGPA/ percentage']>8,'CGPA>8','CGPA<=8')
# df.head(40)

labels= 'CGPA>8' , 'CGPA<=8'
colors= 'cyan','pink'
fig= plt.pie(df['cgpa'].value_counts(),labels=labels,colors=colors,autopct='%1.1f%%')
plt.title('Students in the fourth year whose :')
pdf.savefig()


# In[80]:


plt.close()
plt.clf()


# e) Students who applied for Digital Marketing with verbal and written
# communication score greater than 8.

# In[81]:


df = data.filter(['Areas of interest','Rate your written communication skills [1-10]','Rate your verbal communication skills [1-10]'], axis=1)
df=df.loc[(data['Areas of interest']=='Digital Marketing ')]
df['score']=np.where((df['Rate your written communication skills [1-10]']>8) & (df['Rate your verbal communication skills [1-10]']>8),'scores>8','scores<=8')
# df.head(40)

explode=(0,0.1)
labels= 'verbal and written scores>8' , 'verbal and written scores<=8'
fig= plt.pie(df['score'].value_counts(),labels=labels,autopct='%1.1f%%', explode=explode)
plt.title('Students who applied for Digital Marketing whose :')
pdf.savefig()


# In[82]:


plt.close()


# f) Year-wise and area of study wise classification of students

# In[83]:


df=data.filter(['Major/Area of Study', 'Which-year are you studying in?'],axis=1)
df1=df['Major/Area of Study'].value_counts()
df1


# In[84]:


plt.figure(figsize=(12,8))
df= data.filter(['Major/Area of Study','Which-year are you studying in?'])
df.rename(columns = {'Which-year are you studying in?':'year of study'}, inplace = True)
fig = sns.countplot(y='year of study',hue = 'Major/Area of Study',data = df)
plt.title(label='Year-wise and Area of study wise classification of students')

pdf.savefig()


# In[85]:


plt.close()


# g) City and college wise classification of students.

# In[86]:


df=data.filter(['City', 'College name'],axis=1)
plt.figure(figsize=(8,15))
fig = sns.countplot(y='College name',hue = 'City',data = df)
plt.title(label='City and college wise classification of students')
pdf.savefig()


# In[87]:


plt.close()


# h) Plot the relationship between the CGPA and the target variable.

# In[88]:


df= data['Label'].value_counts()
df


# In[89]:


df=data.filter(['CGPA/ percentage','Label'],axis=1)
df1=df.loc[(df['CGPA/ percentage']<8)]
df2=df.loc[(df['CGPA/ percentage']<9) & (df['CGPA/ percentage']>8)]
df3=df.loc[(df['CGPA/ percentage']<10) & (df['CGPA/ percentage']>9)]


# In[90]:


# df1.head(20)
labels='eligible','ineligible'
colors='skyblue','lightgreen'
fig= plt.pie(df1['Label'].value_counts(),labels=labels,colors=colors,autopct='%1.1f%%')
plt.title('Relationship between target variable and CGPA when it is less than 8')
pdf.savefig()


# In[91]:


labels='eligible','ineligible'
colors='skyblue','lightgreen'
fig= plt.pie(df2['Label'].value_counts(),labels=labels,colors=colors,autopct='%1.1f%%')
plt.title('Relationship between target variable and CGPA when it is less than 9 but greater than 8')
pdf.savefig()


# In[92]:


labels='eligible','ineligible'
colors='skyblue','lightgreen'
fig= plt.pie(df3['Label'].value_counts(),labels=labels,colors=colors,autopct='%1.1f%%')
plt.title('Relationship between target variable and CGPA when it is less than 10 but greater than 9')
pdf.savefig()


# In[93]:


plt.close()


# i) Plot the relationship between the Area of Interest and the target variable.

# In[94]:


df=data.filter(['Areas of interest', 'Label'],axis=1)
plt.figure(figsize=(12,15))
fig = sns.countplot(y='Areas of interest',hue = 'Label',data = df)
plt.title(label='Relationship between the Area of Interest and eligibility')


# In[95]:


plt.close()


# j) Plot the relationship between the year of study, major, and the target variable.

# In[96]:


df=data.filter(['Which-year are you studying in?','Label'],axis=1)

plt.figure(figsize=(10,8))
df.rename(columns = {'Which-year are you studying in?':'year of study'}, inplace = True)
fig = sns.countplot(y='year of study',hue = 'Label',data = df)
plt.title(label='relationship between the year of study and eligibilty')

pdf.savefig()


# In[97]:


df=data.filter(['Major/Area of Study','Label'],axis=1)

plt.figure(figsize=(10,6))
fig = sns.countplot(y='Major/Area of Study',hue = 'Label',data = df)
plt.title(label='relationship between Major/Area of Study and eligibilty')

pdf.savefig()


# In[98]:


plt.close()
