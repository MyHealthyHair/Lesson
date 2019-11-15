#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Screwdriver:
    def __init__(self, size):
        self.size = size
        
    def work(self):
        print('screwing with a screwdriver of size {}...'.format(self.size))
        
class Knife:
    def work(self):
        print('cutting...')
        
class Dog:
    def work(self):
        print('chasing a ball...')
        
class Fork:
    def pick(self):
        print('fork...')
        
class SwissKnife:
    def __init__(self):
        self.tools = {}
        
    def add_tool(self, name, tool):
        if callable(getattr(tool, 'work', None)):
            self.tools[name] = tool
        else:
            print('{} is not a valid tool, work {} not found'.format(name))
        
    def use_tool(self, name):
        tool = self.tools.get(name)
        if tool is not None:
            tool.work()
        else:
            print('{} not found.'.format(name))

sk = SwissKnife()
sk.add_tool('Knife', Knife())
sk.add_tool('Big screwdriver', Screwdriver(10))
sk.add_tool('Small screwdriver', Screwdriver(2))
sk.add_tool('Dog', Dog())
sk.add_tool('Fork', Fork())

sk.use_tool('Big screwdriver')
sk.use_tool('Small screwdriver')
sk.use_tool('Knife')
sk.use_tool('Dog')
sk.use_tool('Fork')


# In[19]:


knife = Knife()
hasattr(knife, 'work')


# In[20]:


hasattr(knife, 'cut')


# In[21]:


setattr(knife, 'cut', None)
callable(getattr(knife, 'cut'))


# In[22]:


callable(getattr(knife, 'screw'))


# In[24]:


knife.__dict__


# In[25]:


from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def work(self):
        pass


# In[ ]:


tool = Tool()


# In[31]:


class Screwdriver(Tool):
    def __init__(self, size):
        self.size = size
        
    def work(self):
        print('screwing with a screwdriver of size {}...'.format(self.size))
        
class Knife(Tool):
    def work(self):
        print('cutting...')
        
class Dog:
    def work(self):
        print('chasing a ball...')
        
class Fork(Tool):
    def pick(self):
        print('picking...')
        
class SwissKnife:
    def __init__(self):
        self.tools = {}
        
    def add_tool(self, name, tool):
        if isinstance(tool, Tool):
            self.tools[name] = tool
        else:
            print('{} is not a valid tool, not derived from class Tool'.format(name))
        
    def use_tool(self, name):
        tool = self.tools.get(name)
        print('{}:'.format(name))
        if tool is not None:
            tool.work()
        else:
            print('not found.')

sk = SwissKnife()
sk.add_tool('Knife', Knife())
sk.add_tool('Big screwdriver', Screwdriver(10))
sk.add_tool('Small screwdriver', Screwdriver(2))
sk.add_tool('Dog', Dog())
# sk.add_tool('Fork', Fork())

sk.use_tool('Big screwdriver')
sk.use_tool('Small screwdriver')
sk.use_tool('Knife')
sk.use_tool('Dog')
# sk.use_tool('Fork')


# In[34]:


from time import sleep
import random

class Bar:
    __empty = '-'
    def __init__(self, length=80):
        self.bar = list()
        for i in range(0, length):
            self.bar,append(Bar.__empty)
            
    def reset(self):
        for i in range(len(self.bar));
            self.bar[i] = Bar.__empty
            
    def update(self, ants):
        self.reset()
        for ant in ants:
            if 0 <= ant.position < len(self.bar):
                self.bar[ant.position] = ant.symbol
                
    def is_empty(self):
        for item in self.bar:
            if not item == Bar.__empty
                return False
        else:
            return True
        
    def show(self):
        for ch in self.bar:
            print(ch, sep='', end='')
        print('', end='\r')
        
class Ant:
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    def __init__(self, position, direction, symbol='*'):
        self.position = position
        self.direction = direction
        if symbol is None:
            self.symbol = Ant.symbols[Ant.count]
            count += 1
        else:
            self.symbol = symbol
        
    def move(self):
        self.position += self.direction
        
    def create_random_ant(length=80):
        position = random.randint(0, length - 1)
        direction = random.choice([1, -1])
        return Ant(position, direction)
    
class Ants:


# In[37]:


try:
    x = int(input('please input a number: '))
    y = int(input('please input a number'))
    print('{}/{} = {}'.format(x, y, x/y))
except ZeroDivisionError:
    print('the second number cannot be 0!')


# In[46]:





# In[ ]:




