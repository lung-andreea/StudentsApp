'''
Created on Nov 27, 2016

@author: Andreea
'''
from src.repository.undo_repo import UndoRepo

'''
Controller for the undo and redo operations
'''
class UndoController(object):
    def __init__(self):
        self.__repo = UndoRepo()
        
    '''
    Function adds a new 3-tuple formed of the current controllers to the undo repository
    '''  
    def save(self,studentController,disciplineController,gradeController):
        return self.__repo.save(studentController,disciplineController,gradeController)
        
    '''
    Function returns the previous 3 controllers (a tuple of 3 elements) from the undo repository 
    '''
    def undo(self):
        return self.__repo.undo()
    
    '''
    Function returns the next 3 controllers (a tuple of 3 elements) from the undo repository 
    '''
    def redo(self):
        return self.__repo.redo()
