'''
Created on Nov 27, 2016

@author: Andreea
'''
from src.domain.validators import UndoRepositoryException

'''
Undo and Redo repository - will store a list of tuples, each of 3 elements representing the controllers used for running the program
'''
class UndoRepo(object):
    def __init__(self):
        self.__repo = []
        self.__counter = [-1]
    
    '''
    Function adds a new 3-tuple formed of the current controllers to the undo repository
    '''  
    def save(self,studentController,disciplineController,gradeController):
        self.__repo[self.__counter[0]+1:] = [(studentController,disciplineController,gradeController)]
        self.__counter[0] = self.__counter[0]+1
        return self.__repo[self.__counter[0]]
    
    '''
    Function returns the previous 3 controllers (a tuple of 3 elements) from the undo repository 
    '''   
    def undo(self):
        if self.__counter[0] == 0:
            raise UndoRepositoryException('No more operations to undo!')
        self.__counter[0] = self.__counter[0]-1
        return self.__repo[self.__counter[0]]
    
    '''
    Function returns the next 3 controllers (a tuple of 3 elements) from the undo repository 
    '''
    def redo(self):
        if self.__counter[0] == len(self.__repo)-1:
            raise UndoRepositoryException('No more operations to redo!')
        self.__counter[0] = self.__counter[0]+1
        return self.__repo[self.__counter[0]]
