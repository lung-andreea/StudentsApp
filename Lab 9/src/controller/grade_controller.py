'''
Created on Nov 5, 2016

@author: Andreea
'''

'''
Class performs the operations implying grades
Arguments:
repository - where the grades are stored 
'''
class GradeController(object):
    def __init__(self,repository):
        self.__repository = repository
        
    @property
    def repository(self):
        return self.__repository
    
    '''
    Sets up a list of grades corresponding to a studentID and a disciplineID 
    (it basically enrolls student having the ID "studentID" to the discipline having the ID "disciplineID")
    ''' 
    def enroll(self,studentID,disciplineID):
        self.__repository.enroll(studentID,disciplineID)
        
    '''
    Adds grade of value "value" to the list of grades corresponding to a studentID and a disciplineID
    '''
    def add(self,studentID,disciplineID,value):
        self.__repository.addGrade(studentID,disciplineID,value)
        
    '''
    Removes all the grades corresponding to a given studentID from the list of grades
    '''
    def removeByStudentID(self,studentID):
        self.__repository.removeGradeByStudentID(studentID)
    
    '''
    Removes all the grades corresponding to a given disciplineID from the list of grades
    '''
    def removeByDisciplineID(self,disciplineID):
        self.__repository.removeGradeByDisciplineID(disciplineID)
    
    '''
    Returns a string representing the list of students enrolled at the discipline with the ID "discID" in alphabetical order
    '''
    def sortStudsAlpha(self,discID):
        return self.__repository.sortStudsAlpha(discID)
    
    '''
    Returns a string representing the list of students enrolled at the discipline with the ID "discID" in descending order 
    of their average grade at that discipline
    '''
    def sortStudsDesc(self,discID):
        return self.__repository.sortStudsDesc(discID)
    
    '''
    Returns a string representing the list of students who fail at at least one discipline (meaning that they have the 
    average grade smaller than 5 at that discipline)
    '''
    def fail(self):
        return self.__repository.fail()
     
    '''
    Returns a string representing the students with the best school situation, meaning all students in descending order of 
    their aggregated average at all disciplines they are enrolled at
    '''   
    def best(self):
        return self.__repository.best()
        
    '''
    Returns a string representing all the disciplines at which there is at least one grade in descending order of the average grade
    received by all students enrolled at that discipline
    '''
    def topDisc(self):
        return self.__repository.topDisc()
    
        