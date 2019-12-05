#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter import ttk


# In[5]:


# Graphical User Interface
def on_click():
    print('hello')
    
button = ttk.Button()
button.pack()
button['text'] = 'Click me!'
button['command'] = on_click

mainloop()


# In[11]:


for i in range(10):
    ttk.Button(text=i).pack(fill=BOTH, expand=True)
    
mainloop()


# In[13]:


for i in range(10):
    ttk.Button(text=i).pack(side=LEFT, fill=BOTH, expand=True)
    
mainloop()


# In[15]:


def on_click():
    label['text'] = 'Clicked'
    
label = ttk.Label(text='hello')
label.pack()
   
button = ttk.Button()
button.pack()
button['text'] = 'Click me!'
button['command'] = on_click

mainloop()


# In[16]:


for i in range(4):
    for j in range(5):
        text = '{}.{}'.format(i, j)
        ttk.Button(text=text).grid(row=i, column=j)
        
mainloop()


# In[ ]:


from tkinter import *
from tkinter import ttk
from enum import Enum

class State(Enum):
    calculated = 0
    in_number1 = 1
    post_operator = 2
    in_number2 = 3
    
class Calculator(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Simple calculator')
        self.geometry('400x600')
        
        self.result_string = StringVar()
        self.result_string.set('0')
        self.number1 = '0'
        self.number2 = None
        self.operator = None
        self.state = State.calculated
        
        # Output
        output = ttk.Label(self, textvariable=self.result_string,
                           font=('TKDefaulFont', 48), anchor=E)
        output.pack(side=TOP, expand=True, fill=BOTH)
        
        # row 1 
        row = Frame(self)
        row.pack(side=TOP, expand=True, fill=BOTH)
        self.add_button(row, 'CE', self.on_ce_click)
        self.add_button(row, 'C', self.on_c_click)
        self.add_button(row, 'Back', self.on_back_click)
        self.add_button(row, '/', self.on_division_click)
        
        # row 2 
        row = Frame(self)
        row.pack(side=TOP, expand=True, fill=BOTH)
        self.add_button(row, '7', self.gen_on_number_click('7'))
        self.add_button(row, '8', self.gen_on_number_click('8'))
        self.add_button(row, '9', self.gen_on_number_click('9'))
        self.add_button(row, 'x', self.on_multiply_click)
        
        # row 3 
        row = Frame(self)
        row.pack(side=TOP, expand=True, fill=BOTH)
        self.add_button(row, '4', self.gen_on_number_click('4'))
        self.add_button(row, '5', self.gen_on_number_click('5'))
        self.add_button(row, '6', self.gen_on_number_click('6'))
        self.add_button(row, '-', self.on_minus_click)

        # row 4 
        row = Frame(self)
        row.pack(side=TOP, expand=True, fill=BOTH)
#        self.add_button(row, '1', self.on_1_click)
        self.add_button(row, '1', self.gen_on_number_click('1'))
        self.add_button(row, '2', self.gen_on_number_click('2'))
        self.add_button(row, '3', self.gen_on_number_click('3'))
        self.add_button(row, '+', self.on_add_click)

        # row 5 
        row = Frame(self)
        row.pack(side=TOP, expand=True, fill=BOTH)
        self.add_button(row, '+/-', self.on_negative_click)
        self.add_button(row, '0', self.gen_on_number_click('0'))
        self.add_button(row, '.', self.gen_on_number_click('.'))
        self.add_button(row, '=', self.on_equal_click)
        
    def add_button(self, parent, text=None, command=None):
        button = ttk.Button(parent, text=text, command=command)
        button.pack(side=LEFT, expand=True, fill=BOTH)
        
    def on_ce_click(self):
        print('ce clicked.')
        
    def on_c_click(self):
        print('c clicked.')

    def on_back_click(self):
        print('back clicked.')

    def on_division_click(self):
        self.on_operator('/')
        print('division clicked.')

    def gen_on_number_click(self, ch):
        return lambda: self.on_number(ch)
    
#    def on_1_click(self):
#        self.on_number('1')
#        print('1 clicked.')

    def on_number(self, ch):
        print(self.state)
        if self.state == State.calculated:
            self.number1 = ch
            self.state = State.in_number1
            self.result_string.set(self.number1)
        elif self.state == State.in_number1:    
            self.number1 = self.number1 + ch
            self.result_string.set(self.number1)
        elif self.state == State.post_operator:
            self.number2 = ch
            self.state = State.in_number2
            self.result_string.set(self.number2)
        elif self.state == State.in_number2:
            self.number2 = self.number2 + ch
            self.result_string.set(self.number2)
        else: assert(0)
    
   
    def on_multiply_click(self):
        print('x clicked.')
        self.on_operator('*')
    
    def on_minus_click(self):
        print('- clicked.')
        self.on_operator('-')

    def on_add_click(self):
        print('+ clicked.')
        self.on_operator('+')
    
    def on_operator(self, operator):
        if self.state == State.calculated:
            self.state = State.post_operator
        elif self.state == State.in_number1:
            self.state = State.post_operator
        # elif self.state == State.post_operator:
        elif self.state == State.in_number2:
            self.on_equal_click()
            self.state = State.post_operator
        else: assert(0)        

        self.operator = operator
    
    def on_equal_click(self):
        if self.state != State.in_number2:
            return 
        
        print('= clicked.')
        if self.operator == '+':
            self.number1 = str(float(self.number1) + float(self.number2))
        elif self.operator == '-':
            self.number1 = str(float(self.number1) - float(self.number2))
        elif self.operator == '*':
            self.number1 = str(float(self.number1) * float(self.number2))
        elif self.operator == '/':
            self.number1 = str(float(self.number1) / float(self.number2))

        self.result_string.set(self.number1)
        self.state = State.calculated

    def on_negative_click(self):
        print('+/- clicked.')
        
if __name__ == '__main__':
    app = Calculator()
    app.mainloop()


# In[ ]:




