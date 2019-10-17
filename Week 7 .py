#!/usr/bin/env python
# coding: utf-8

# In[1]:


d = dict()
d['b'] = 1
d.setdefault('a', 0)
d.setdefault('b', 0)
print(d)pir


# In[2]:


count = {}
for ch in 'hello world':
    if count.get(ch) == None:
        count[ch] = 0
    else:
        count[ch] = count[ch] + 1
print(count)


# In[4]:


x,y = 1,2
print(x,y)


# In[5]:


x, y = y , x
print(x, y)


# In[6]:


x, y ,z = 1, 2, 3
print(x, y ,z)


# In[8]:


r = 1, 2, 3
x, y, z = (1, 2, 3)
print(1, 2, 3)


# In[9]:


x, y, *r = 1, 2, 3, 4
print(x, y, r)


# In[10]:


x, *m, y = 1, 2, 3, 4, 5
print(x, y, m)


# In[11]:


x, *m, y = 'hello world'
print(x, y, m)


# In[12]:


x = y = 3
print(x,y)


# In[ ]:


x = 3
y = 3


# In[13]:


x = y = [1,2]
x[0] = 0
print(x,y)


# In[14]:


x is y


# In[15]:


x = [1,2]
y = [1,2]
x is y


# In[16]:


x = (1,2)
y = (1,2)
x is y


# In[17]:


x = 'hello'
y = 'hello'
x is y


# In[18]:


a = 0
a += 1
a


# In[19]:


a = 0
a = a+1
a


# In[22]:


a = [1,2]
b = a
print(a is b)
a = a + [3]
print(a)
print(a is b)


# In[23]:


a = [1,2]
b = a
print(a is b)
a += [3]
print(a)
print(a is b)


# In[24]:


b


# In[ ]:


if a > b:
    print(a)


# In[25]:


True, False
True + 1


# In[26]:


int(True)


# In[28]:


name = input('please enter your name: ')
if name:
    print('hello, ' + name)
else:
    print('Forget your name?')


# In[29]:


def abs(a):
    return a if a >= 0 else -a
print(abs(-3), abs(3), abs(0))


# In[31]:


name = input('please enter your name: ')
print('hello, ' + name if name else 'Forget your name?')


# In[32]:


a = [1, 2, 3]
1 in a


# In[33]:


for i in range(0, 10):
    print('*', end='')


# In[1]:


year = int(input('Please enter a year: '))
if year % 400 == 0:
    print('yes')
elif year % 100 ==0:
    print('not')
elif year % 4 == 0:
    print('not')
else:
    print('not')


# In[3]:


def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 ==0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
year = int(input('enter a year ; '))
if year < 0:
    print('invalid year')
else:
    print('leap year' if leap_year(year) else 'not leap year')
 


# In[6]:


assert(4 == 4)


# In[8]:


def leap_year(year):
    assert(year >= 0)
    if (year % 400 == 0) or (year % 4 == 0 and year % 100):
        return True
    else:
        return False
    
    if year % 400 == 0:
        return True
    elif year % 100 ==0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
assert(leap_year(2000) == True)
assert(leap_year(1980))
assert(leap_year(1000) == False)
assert(not leap_year(1987))
print('test ok')


# In[9]:


chr(98)


# In[10]:


chr(128584)


# In[11]:


chr(128585)


# In[12]:


chr(128590)


# In[17]:


chr(1000)


# In[18]:


for i in range(0,5):
    print('*' * 10)


# In[20]:


i = 0
while i < 5:
    print('*' * 10)
    i += 1


# In[22]:


import math
x = 1
while x < 60:
    print('\b *', end='')
    y = 0
    while y < 500000:
        z = math.sin(x) * math.exp(x)
        y += 1
    x += 1
        


# In[ ]:




