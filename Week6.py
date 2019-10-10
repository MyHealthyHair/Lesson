#!/usr/bin/env python
# coding: utf-8

# In[1]:


names = ['zhangsan','lisi','wangwu','maliu']
scores = [100,90,80,70]
name = input('please input a name')
print(scores[names.index(name)])


# In[2]:


scores = {'zhangsan':100,'lisi':90,'wangwu':80,'maliu':70}
name = input('please enter a name')
print(scores[name])


# In[3]:


def add(a,b):
    return a + b

print(add(3,4))


# In[ ]:




