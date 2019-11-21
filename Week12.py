#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bird:
    def __init__(self):
        self.hungry = True
        
    def eat(self):
        if self.hungry:
            print('Aaaah....')
            self.hungry = False
        else:
            print('No, thanks.')
            
b = Bird()
b.eat()


# In[2]:


b.eat()


# In[5]:


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawki!'
        
    def sing(self):
        print(self.sound)
        
s = SongBird()
s.sing()
s.eat()


# In[9]:


class A:
    def __init__(self):
        self.a = 'a'
        
class B(A):
    def __init__(self):
        super().__init__()
        self.b = 'b'
        
class C(B):
    def __init__(self):
        super().__init__()
        self.c = 'c'
        
    def test(self):
        print(self.a, self.c)
        
c = C()
c.test()


# In[ ]:


class Hamburger:
    def __init__(self):
        self.meat = 'beef'
        self.toppings = ['tomato','bacon','onion ring']
        condiments = ['lime sour sauce']

beef_hamburger = Hamburger()
beaf_hamburger.toppings = ['tomato', 'lettuce']
beaf_condiments = ['mayo']

chicken_hamburger = Hamburger()
chicken_hamburger.meat = 'chicken'
chicken_hamburger.toppings = ['red pepper', 'lettuce']
chicken_condiments = ['BBQ source']


# In[10]:


# __len(self)__
len('hello')


# In[ ]:


# __getitem__(self, key)
my_list = [1, 2, 3]
print(my_list[0])

# __setitem__(self, key)
my_list[0] = 2 

# __delitem__(self, key)
del my_list[0]


# In[ ]:


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}
        
    def check_key(key):
        if not isinstance(key, int): raise TypeError
        if key < 0: rasie IndexError
       
    def __getitem__(self, key):
        ArithmeticSequence.check_key
        try: 
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step
    
    def __setitem__(self, key, value):
        ArithmeticSequence.check_key(key)
        self.changed[key] = value


# In[ ]:


s = ArithmeticSequence(1, 2)
print(s[4])
print(s[10000])
s[4] = 100


# In[13]:


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
        
    def __next__(self):
        self.a, self.b = self.b, self.a +self.b
        return self.a
    
    def __iter__(self):
        return self
    
for i in Fibs():
    print(i, end=' ')
    if i > 10000: break


# In[ ]:


class Fibs:
    def __init__(self, max):
        self.a = 0
        self.b = 1
        self.max = max
        
    def __next__(self):
        self.a, self.b = self.b, self.a +self.b
        if self.a > self.max: raise StopIteration
        return self.a
    
    def __iter__(self):
        return self


# In[17]:


for i in Fibs(1000):
    print(i, end= ' ')qq


# In[16]:


it = iter([1, 2, 3])
next(it)


# In[ ]:




