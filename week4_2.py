#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
count = [0] * 6
number_of_tests = 60000
last_three = [3,3,3]
for i in range(0,number_of_tests):
    last_three.append(random.randint(1,6))
    last_three.pop(0)
    if(last_three[0] == last_three[1] == last_three[2]):
        count[last_three[2] - 1] += 1

print(count)


# In[7]:


a = (1,2,3)
a[0]
1
a[0] = 0


# In[8]:


a = (42, )
a
