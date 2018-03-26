'''
Created on Nov 4, 2016

@author: Andreea
'''

class RepositoryException(Exception):
    pass

class UndoRepositoryException(RepositoryException):
    pass

class InputValidator(object):
    @staticmethod
    def isFloat(nr):
        try:
            float(nr)
            return True
        except ValueError:
            return False
        
    @staticmethod    
    def isInteger(nr):
        try:
            int(nr)
            return True
        except ValueError:
            return False
    
    @staticmethod    
    def hasNumbers(s):
        return any(c.isdigit() for c in s)