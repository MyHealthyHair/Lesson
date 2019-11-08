#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Person:
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def greet(self):
        print("hello, I am {}.".format(self.name))
        
zs = Person()
zs.set_name('ZA ss')
zs.greet()
ss = Person()
ss.set_name('XX')
ss.greet()


# In[28]:


class Person:
    count = 0
    
    def __init__(self, name=None):
         self._name = name
        Person.count += 1
        print('Total number of person: {}'.format(Person.count))
        
    def set_name(self, name):
        # assert(name, str)
        isinstance(name, str)
            self._name = name
        else:
            print('not a valid name.')
    
    def get_name(self):
        return self._name
    
    def greet(self):
        print("hello, I am {}.".format(self._name))
        
dd = Person('dd')
ff = Person('ff')
dd.greet()
ff.greet()
ww = Person()


# In[17]:


dd.name = 'text'
dd.greet()
dd.set_name(1)


# In[29]:


help(Person)


# In[31]:


class Cat:
    def meow(self):
        print('meow...')
        
class Dog:
    def wong(self):
        print('wong...')
        
pets = list()
pets.append(Cat())
pets.append(Dog())

for item in pets:
    if isinstance(item, Cat):
        item.meow()
    elif isinstance(item, Dog):
        item.wong()
    else:
        pass


# In[33]:


class Cat:
    def talk(self):
        print('meow...')
        
class Dog:
    def talk(self):
        print('wong...')
        
pets = [Cat(), Dog(), Cat()]

for item in pets:
    item.talk()


# In[34]:


def add(a, b):
    return a + b

a = 1
b = 2
print(add(a, b))
x, y = 'a', 'b'
print(add(x, y))


# In[35]:


class Student(Person):
    def set_score(self, score):
        self.__score = score
        
    def get_score(self):
        return self.__score
    
    def show_score(self):
        print('My score is: {}'.format(self.__score))
        
dd = Student()
dd.set_name('dd')
dd.set_score(100)
dd.greet()
dd.show_score()


# In[39]:


class Filter():
    def __init__(self):
        self.__blocked = []
        
    def filter(self, sequence):
        return [x for x in sequence if x not in self.__blocked]
    
class SpamFilter(Filter):
    def __init__(self):
        self.__blocked = ['SPAM']
        
f = Filter()
f.filter([1, 2, 3])


# In[ ]:




