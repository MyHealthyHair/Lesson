#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1,10):
    print('{}^3={}'.format(i,i**3))


# In[3]:


for i in range(0,10):
    print(' '*(9-i),'*'*(2*i+1))


# In[6]:


for i in range(0,10):
    print('+'*(9-i),'*'*(2*i+1))


# In[10]:


for i in range(0,10):
    print('+'*(9-i),'*'*(2*i+1),sep='')


# In[11]:


a = list(range(1,10))
print(a)
del a[0]
print('after del: ',a)


# In[12]:


a.clear()
print(a)


# In[13]:


a = range(1,4)
b = a
print('a; ',a)
print('b: ',b)


# In[14]:


a = list(range(1,4))
b = a
print('a; ',a)
print('b: ',b)


# In[15]:


del b[0]
print('a: ',a)
print('b: ',b)


# In[16]:


a = list(range(1,4))
b = a.copy()
print('a: ',a)
print('b: ',b)


# In[17]:


b.append(4)
print('a: ',a)
print('b: ',b)


# In[18]:


a = [1,2,3,[4,5]]
a[3][0]


# In[19]:


b = a.copy()
print('a: ',a)
print('b: ',b)


# In[20]:


a[3][0] = 4.1
print('a: ',a)
print('b: ',b)


# In[22]:


from copy import deepcopy
a = [1,2,3,[4,5]]
b = deepcopy(a)
print('a: ',a)
print('b: ',b)


# In[23]:


a[3][0] = 4.1
print('a: ',a)
print('b: ',b)


# In[24]:


a=[1,2,3,3,5,7]
a.count(3)


# In[25]:


len(a)


# In[26]:


a.index(1)


# In[27]:


a.index(8)


# In[30]:


a.insert(2,'*')
print(a)


# In[29]:


a.remove('*')
print(a)


# In[31]:


a = [1,2,3]
a.append(4)
a


# In[32]:


a.pop()
a


# In[33]:


a.pop()
a


# In[34]:


a.append(5)
a


# In[37]:


expression = input('please input an expression: ')

my_stack = list()

left_quotes=['{','[','(']
right_quotes=['}',']',')']

for ch in expression:
    if ch in left_quotes:
        my_stack.append(ch)
    elif ch in right_quotes:
        if my_stack == []:
            print('not  match')
        else:
            left_ch = my_stack.pop()
            if (left_quotes.index(left_ch) != right_quotes.index(ch)):
                print('not match')
                break
if my_stack != []:
    print('not match')
else:
    print('match')


# In[38]:


a = [1,2,3]
b = [4,5,6]
print(a+b)


# In[39]:


a = a+b
print(a)


# In[40]:


a += b
print(a)


# In[42]:


a = 'hello'
b = ' world'
print(a + b)


# In[43]:


a = [1,2,3]
a.append([4,5,6])
a


# In[44]:


a = list(range(0,6))
print(a)
a.reverse()
print('a after reverse(): ',a)


# In[45]:


b = a.reverse()
print(b)


# In[ ]:


b = a.copy()
b.reverse()


# In[46]:


import random
for i in range(0,20):
    value = random.randint(1,6)
    print(value, end=' ')


# In[48]:


import random
a = list()
for i in range(0,20):
    value = random.randint(1,6)
    a.append(value)
    
print(a)


# In[49]:


a.sort()
print(a)


# In[52]:


import random
a = [None] * 20
for i in range(0,20):
    a[i] = random.randint(1,6)
print(a)


# In[54]:


get_ipython().run_cell_magic('timeit', '', 'a = [None] *10000\nfor i in range(0,10000):\n    a[i] = i')


# In[58]:


get_ipython().run_cell_magic('timeit', '', 'a = []\nfor i in range(0,10000):\n    a.append(i)')


# In[67]:


import random
a = [None] * 100
for i in range(0,100):
    a[i] = random.randint(1,6)

print('mean: ',sum(a)/len(a))
print('max: ',max(a) )
print('min: ',min(a))


# In[ ]:


month = int(input('please input the month: '))
day = int(input('please input the day: '))

count = day
if month > 1:
    count += 31
if month > 2:
    count += 28
if month > 3:
    count += 31
if month > 4:
    count += 30
if month > 5:
    count += 31
if month > 6:
    count += 30
if month > 7:
    count += 31
if month > 8:
    count += 31
if month > 9:
    count += 30
if month > 10:
    count += 31
if month > 11:
    count += 30
if month > 12:
    count += 31
print('this is the {}th day in the year.'.format(count))


# In[ ]:


month = int(input('please input the month: '))
day = int(input('please input the day: '))

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

count = day

i = 1
while i < month:
    count += days_in_month[i - 1]
    i += 1
    
print('this is the {}th day in the year.'.format(count))


# In[ ]:


import random
count = [0] * 6
for i in range(0,60000):
    value = random.randint(1,6)
    count[value - 1] += 1

print(count)
print((max(count) - min(count)) * 6 / sum(count))
