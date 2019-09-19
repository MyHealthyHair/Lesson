#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=float(input('please input a number:'))
b=float(input('please input a number:'))
print('{}+{}={}'.format(a,b,a+b))


# In[3]:


2/3


# In[7]:


sum=0
x=1
while x<101:
    sum=sum+x
    x=x+1
    
print(sum)


# In[12]:


answer=input("do you like python?(y/n)")
while answer !='y':
    print('do not be joking')
    answer=input('do you like python?(y/n)')
print("how billrant you are!")


# In[13]:


2+3+4+5+6+7


# In[14]:


"你好".encode('ASCII')


# In[15]:


"你好".encode('MBCS')


# In[16]:


len("你好".encode('MBCS'))


# In[17]:


"hello".encode('UTF-8')


# In[18]:


"你好".encode('UTF-8')


# In[21]:


for row in range(1,10):
    for column in range(1,10):
        
            print('{}*{}={}'.format(row,column,row*column),end='\t')
        
    print(' ')


# In[23]:


for row in range(1,10):
    for column in range(1,10):
        if column >= row:
            print('{}*{}={}'.format(row,column,row*column),end='\t')
        else:
            print(' ',end='\t')
    print(' ')

