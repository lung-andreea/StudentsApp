'''
Created on Nov 4, 2016

@author: Andreea
'''

'''
Entity class - can be either a Student or a Discipline having an ID and a name
'''
class Entity(object):
    def __init__(self, ID, name):
        self.__ID = ID
        self.__name = name
        
    @property
    def ID(self):
        return self.__ID
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value
    
        
'''
Grade class having a StudentID, a DisciplineID and a list of grades corresponding to that StudentID and DisciplineID
'''
class Grade(object):
    def __init__(self,StudentID,DisciplineID,value):
        self.__studentID = StudentID
        self.__disciplineID = DisciplineID
        self.__value = value
        
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self,val):
        self.__value = val
    
    @property
    def studentID(self):
        return self.__studentID
    
    @property
    def disciplineID(self):
        return self.__disciplineID