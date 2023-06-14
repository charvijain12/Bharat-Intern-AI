#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import spacy
import nltk
import matplotlib.pyplot as plt
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
import string
import re


# ### Displaying the skills required

# In[18]:


skills="Data mining or extracting usable data from valuable data sources Using machine learning tools to select features, create and optimize classifiers Carrying out preprocessing of structured and unstructured data Enhancing data collection procedures to include all relevant information for developing analytic systems Processing, cleansing, and validating the integrity of data to be used for analysis Analyzing large amounts of information to find patterns and solutions Developing prediction systems and machine learning algorithms Presenting results in a clear manner Propose solutions and strategies to tackle business challenges Collaborate with Business and IT teams Become a Data Science Expert & Get Your Dream Job Professional Certificate Program In Data ScienceEXPLORE PROGRAMBecome a Data Science Expert & Get Your Dream Job Data Scientist Skills You need to master the skills required for data scientist jobs in various industries and organizations if you want to pursue a data scientist career. Let’s look at the must-have data scientist qualifications. Key skills needed to become a data scientist: Programming Skills – knowledge of statistical programming languages like R, Python, and database query languages like SQL, Hive, Pig is desirable. Familiarity with Scala, Java, or C++ is an added advantage. Statistics – Good applied statistical skills, including knowledge of statistical tests, distributions, regression, maximum likelihood estimators, etc. Proficiency in statistics is essential for data-driven companies. Machine Learning – good knowledge of machine learning methods like k-Nearest Neighbors, Naive Bayes, SVM, Decision Forests. Strong Math Skills (Multivariable Calculus and Linear Algebra) - understanding the fundamentals of Multivariable Calculus and Linear Algebra is important as they form the basis of a lot of predictive performance or algorithm optimization techniques. Data Wrangling – proficiency in handling imperfections in data is an important aspect of a data scientist job description. Experience with Data Visualization Tools like matplotlib, ggplot, d3.js., Tableau that help to visually encode data Excellent Communication Skills – it is incredibly important to describe findings to a technical and non-technical audience. Strong Software Engineering Background Hands-on experience with data science tools Problem-solving aptitude Analytical mind and great business sense Degree in Computer Science, Engineering or relevant field is preferred Proven Experience as Data Analyst or Data Scientist"
skills


# ### Preprocessing of skills data

# In[19]:


text_nonpunc=''.join([char for char in skills if char not in string.punctuation])
skills=text_nonpunc
tokens=re.split('\W+',skills)
skills=tokens
stop_words=set(stopwords.words('english'))
re_sw=[word for word in skills if word not in stop_words]
skills=re_sw
ln=nltk.WordNetLemmatizer()
lemm=[ln.lemmatize(word) for word in skills]
skills=lemm


# In[20]:


nlp = spacy.load("en_core_web_sm")
doc=nlp(' '.join([char for char in skills]))
def tot_list(text):
  return set(' '.join([char for char in text]).lower().split(' '))
skills_list=set(' '.join([chunk.text for chunk in doc.noun_chunks]+[token.lemma_ for token in doc if token.pos_ == "VERB"]+[entity.text for entity in doc.ents]).lower().split(' '))


# ### Displaying the skills list

# In[21]:


skills_list


# ### Loading the dataset

# In[22]:


df=pd.read_csv('UpdatedResumeDataSet.csv')


# In[23]:


df.head()


# In[24]:


df.info()


# ### There are total 962 records in dataset without any null values

# ### Column Overview

# 1. Category = It describes about the role/field of the job which the applicants are insterested in
# 
# 2. Resume = It consists of the skills mentioned by the candidates

# In[25]:


df['Category'].value_counts()


# In[26]:


len(df['Category'].value_counts())

