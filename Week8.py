#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [1, 2, 3]
b = a
del a 
b


# In[4]:


exec('print("hello world")')


# In[6]:


def hello(name):
    'say to somebody whose name is defined by name'
    print('hello, ' + name + '!')


# In[7]:


callable(hello)


# In[8]:


hello('kk')


# In[9]:


print(hello('kk'))


# In[16]:


def print_banner(text, width):
    symbol = '#'
    print(symbol * width)
    print(text.center(width - 2).center(width, symbol))
    print(symbol * width)
    
print_banner('hello', 30)


# In[17]:


fibs = [1, 1]
for i in range(0, 9):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)


# In[18]:


print(fibs[5])


# In[19]:


def fibs(num):
    result = [1, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result

num = int(input('how many fibonacci numbers do you want?'))
print(fibs(num))


# In[25]:


def fib(index):
    item_before_last, last_item = 1, 1
    for i in range(index - 2):
        item_before_last, last_item = last_item, item_before_last + last_item
    return last_item

num = int(input('how mant steps?'))
print('total number of different ways: {}'.format(fib(num)))


# In[26]:


def change_it(a):
    a = a * 2
    
x = 2
change_it(x)
print(x)


# In[28]:


def change_it(a):
    # a[0] = 'hello'
    a[0] = 'hello'
x = ['hello', 'hi']
change_it(x)
print(x)


# In[ ]:


def change_it(a):
    a[0] = 'H'
x = ['hello', 'hi']
change_it(x)
print(x)


# In[29]:


def hello(greeting, name):
    print('{}, {}!'.format(greeting, name))
    
hello('hi', 'world')
hello('world', 'hi')


# In[30]:


def interval(start, end=None, step=1):
    if end is None:
        start, end=0, start
    result = []
    i = start
    while i < end:
        result.append(i)
        i += step
    return result

print(interval(8))
print(interval(2, 8))
print(interval(2, 8, 2))


# In[31]:


def sum(*params):
    result = 0
    for item in params:
        result += item
    return result

assert(sum(1, 2, 3, 4) == 10)
print('ok')


# In[35]:


def print_sum(*params, label='Sum'):
    result = 0
    for item in params:
        result += item
        
    print(label, result)

print_sum(1, 2, 3, 4, label='和')


# In[ ]:




