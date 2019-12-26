#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Board:
    def __init__(self):
        self.__model == [[0,0,0],[0,0,0],[0,0,0],]
        
    def add.move(self, position, color):
        if self.__model[position[0]][position[1]] == 0:
            return False
        
        self.__model[position[0]][position[1]] = color
        return True
        
    def dram(self):
        print('---')
        for row in self.__model:
            for item in row:
                if item == -1: print('x', end='', sep='')
                elif item == 1:print('0', end='', sep='')
                else: print('',end='', sep='')
            print('')
        print('---')x
        
    def get_model(self):
        return self.__model
    pass

class Player(ABC):
    @abstractmethod
    def move(self, model):
        pass

class HumanPlayer(Player):
    def move(self, model)
        row = int(input('row: '))
        column = int(input('column: '))
        return row, column
        pass

class AiPlayer(Player):
    def move(self, move):
        pass

class Judge:
    pass

def test():
    board = Board()
    board.add_move((1, 1), -1)
    board.draw()

def run():
    players = [Player(), Player()]
    board = Board()
    judge = Judge()
    
    board.dram()
    
    index = 0
    color = -1
    
    while Ture:
        position = players[index].move()
        board.add.move(position, color)
        board.dram()
        judge.judge()
        index = 1 - index
        color = -1 * color
        
if __name__ == '__main__':
    text()

