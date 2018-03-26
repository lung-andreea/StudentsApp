'''
Created on Nov 6, 2016

@author: Andreea
'''

from src.domain.entities import Grade
from src.domain.validators import RepositoryException
from src.domain.utile import shellSort
from src.domain.utile import filterMethod
from _collections_abc import Iterable

'''
Repository to store the list of all objects x (x = Grade(studentID,disciplineID)) where x 
is a valid grade corresponding to a student and a discipline
'''
class GradeRepository(Iterable):
    
    def __init__(self,students,disciplines,enrolled,grades):
        self.__grades = grades
        self.enrolled = enrolled
        self.students = students
        self.disciplines = disciplines
        
    def __iter__(self):
        return self.__grades
    
    def __next__(self,i):
        return self.__grades[i+1]
    
    def __setItem__(self,i,value):
        self.__grades[i] = value
        
    def __delItem__(self,i):
        del self.__grades[i]
        
    @property
    def grades(self):
        return self.__grades
    
    @grades.setter
    def grades(self,grades):
        self.__grades[:] = grades
    
    '''
    Enrolls student having the ID studentID to the discipline having the ID disciplineID
    ''' 
    def enroll(self,studentID,disciplineID):
        if not studentID in self.students.entities:
            raise RepositoryException('Student ID does not exist!')
        if not disciplineID in self.disciplines.entities:
            raise RepositoryException('Discipline ID does not exist!')
        if self.isEnrolled(studentID,disciplineID):
            raise RepositoryException('\nStudent is already enrolled at this discipline!\n')
        self.enrolled.append((studentID,disciplineID))
        
    def deEnrollStudent(self,studentID):
        self.enrolled[:] = filterMethod(self.enrolled, lambda x: not x[0] == studentID)
        
        
    def deEnrollDiscipline(self,disciplineID):
        self.enrolled[:] = filterMethod(self.enrolled, lambda x: not x[1] == disciplineID)
        
    '''
    Function returns True if teh student with the ID "studentID" is enrolled at the discipline the ID "disciplineID" and False otherwise
    '''     
    def isEnrolled(self,studentID,disciplineID):
        for x in self.enrolled:
            if x[0] == studentID and x[1] == disciplineID:
                return True
        return False   
        
    '''
    Assigns a new grade "value" to the student having the ID "studentID" at the discipline with the ID "disiciplineID"
    Raises:
    RepositoryException - if there is no student with specified ID
                          if there is no discipline with specified ID
                          if the student is not enrolled at that discipline
    '''
    def addGrade(self,studentID,disciplineID,value):
        if not studentID in self.students.entities:
            raise RepositoryException('Student ID does not exist!')
        if not disciplineID in self.disciplines.entities:
            raise RepositoryException('Discipline ID does not exist!')
        if not self.isEnrolled(studentID,disciplineID):
            raise RepositoryException('\nStudent is not enrolled at discipline {0}\n'.format(disciplineID))
        grade = Grade(studentID,disciplineID,value)
        self.__grades.append(grade)
    
    '''
    Removes all the grades corresponding to a given studentID from the list of grades
    '''
    def removeGradeByStudentID(self,studentID):
        self.__grades[:] = filterMethod(self.__grades,lambda x: not x.studentID == studentID)
     
    '''
    Removes all the grades corresponding to a given disciplineID from the list of grades
    '''   
    def removeGradeByDisciplineID(self,disciplineID):
        self.__grades[:] = filterMethod(self.__grades, lambda x: not x.disciplineID == disciplineID)
    
    '''
    Returns a string representing the list of students enrolled at the discipline with the ID "discID" in alphabetical order
    ''' 
    def sortStudsAlpha(self,disciplineID):
        studs =[]
        l = shellSort(self.listOfStudEnrolledAt(disciplineID), lambda x,y: self.students.findByID(x)<self.students.findByID(y))
        for x in l:
            studs.append((x,self.students.findByID(x)))
        return studs    
    
    '''
    Returns a string representing the list of students enrolled at the discipline with the ID "discID" in descending order 
    of their average grade at that discipline
    '''
    def sortStudsDesc(self,disciplineID):
        studs = []
        l = filterMethod(self.listOfStudEnrolledAt(disciplineID),lambda x: not self.avg(x,disciplineID) == 0)
        l = shellSort(l, lambda x,y: self.avg(x,disciplineID)>self.avg(y, disciplineID))
        for x in l:
            studs.append((x,self.students.findByID(x),self.avg(x,disciplineID)))
        return studs
    
    '''
    Returns a string representing the list of students who fail at at least one discipline (meaning that they have the 
    average grade smaller than 5 at that discipline)
    '''    
    def fail(self):
        failList = []
        for x in self.students.entities:
            for y in self.listOfDisciplinesStudentIsEnrolledAt(x):
                if self.avg(x,y) < 5 and not self.avg(x,y) == 0:
                    failList.append((x,self.students.findByID(x)))
                    break
        return failList
    
    '''
    Returns a string representing the students with the best school situation, meaning all students in descending order of 
    their aggregated average at all disciplines they are enrolled at
    '''  
    def best(self):
        best = []
        l = filterMethod(self.students.entities.keys(), lambda x: not self.totalAvg(x) == 0)
        l = shellSort(l, lambda x,y: self.totalAvg(x)>self.totalAvg(y))
        for x in l:
            best.append((x,self.students.findByID(x),self.totalAvg(x)))
        return best
    
    '''
    Returns a string representing all the disciplines at which there is at least one grade in descending order of the average grade
    received by all students enrolled at that discipline
    '''
    def topDisc(self):
        topDisc = []
        l = filterMethod(self.disciplines.entities.keys(), lambda x: not self.avgByDisciplineID(x) == 0)
        l = shellSort(l, lambda x,y: self.avgByDisciplineID(x)>self.avgByDisciplineID(y))
        for x in l:
            topDisc.append((x,self.disciplines.findByID(x),self.avgByDisciplineID(x)))
        return topDisc
    
    '''
    Returns a list of the student IDs who are enrolled at the discipline with the ID "disciplineID" 
    '''
    def listOfStudEnrolledAt(self,disciplineID):
        return [x[0] for x in self.enrolled if x[1] == disciplineID]
    
    '''
    Returns a list of the discipline IDs the student with the ID "studentID" is enrolled at
    '''
    def listOfDisciplinesStudentIsEnrolledAt(self,studentID):
        return [x[1] for x in self.enrolled if x[0] == studentID]
    
    '''
    Calculates and returns the average grade received by the student with the ID "studentID" at all disciplines he is enrolled at
    '''
    def totalAvg(self,studentID):
        s = 0
        l = len(self.listOfDisciplinesStudentIsEnrolledAt(studentID))
        for x in self.listOfDisciplinesStudentIsEnrolledAt(studentID):
            if self.avg(studentID,x) == 0:
                l-= 1
            s+= self.avg(studentID,x)
        if l == 0:
            return 0
        return float('{:.2f}'.format(s/l))
    
    '''
    Calculates and returns the average grade received by all students enrolled at the discipline with the ID "disciplineID"
    '''
    def avgByDisciplineID(self,disciplineID):
        s = 0
        l = len(self.listOfStudEnrolledAt(disciplineID))
        for x in self.listOfStudEnrolledAt(disciplineID):
            if self.avg(x,disciplineID) == 0:
                l-= 1
            s+= self.avg(x,disciplineID)
        if l == 0:
            return 0
        return float('{:.2f}'.format(s/l))
    
    '''
    Calculates and returns the average grade received by the student with the ID "studentID" at the discipline with the ID "disicplineID"
    Returns:
    0 - if student is not enrolled at that dicipline or he doesn't have any grades at that discipline 
    '''   
    def avg(self,studentID,disciplineID):
        s,nr = 0,0
        for x in self.__grades:
            if x.studentID == studentID and x.disciplineID == disciplineID:
                s+= x.value
                nr+= 1
        if nr == 0:
            return 0
        return float('{:.2f}'.format(s/nr))
    

        
