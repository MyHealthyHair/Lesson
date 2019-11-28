#!/usr/bin/env python
# coding: utf-8

# In[3]:


class MyClass:
    def static_method():
        print('This is a static method.')
    static_method = staticmethod(static_method)
    
    def class_method(cls):
        print('This is a class method of: ', cls)
    class_method = classmethod(class_method)
    
MyClass.static_method()
MyClass.class_method()


# In[6]:


import copy
dir()


# In[7]:


copy.__all__


# In[8]:


help(copy.deepcopy)


# In[9]:


copy.__file__

