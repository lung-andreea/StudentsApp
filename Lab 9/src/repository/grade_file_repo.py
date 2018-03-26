'''
Created on Dec 11, 2016

@author: Andreea
'''
import pickle

from src.domain.entities import Grade
from src.repository.grade_repository import GradeRepository


class GradeFileRepository(GradeRepository):

    def __init__(self, enrolledFileName, gradeFileName):
        super().__init__([],[],[],[])
        self.__enrolledFile = enrolledFileName
        self.__gradeFile = gradeFileName
        
    def writeToFile(self,enrolled,grades):
        f = open(self.__enrolledFile,'w')
        g = open(self.__gradeFile, 'w')
        try:
            for x in enrolled:
                string = str(x[0])+' '+str(x[1])+'\n'
                f.write(string)
            f.close()
            for x in grades:
                string = str(x.studentID) +' '+str(x.disciplineID)+' '+str(x.value)+'\n'
                g.write(string)
            g.close()
        except Exception as e:
            print('The following error occured '+str(e))
            
    def readEnrolled(self):
        f = open(self.__enrolledFile, 'r')        
        result = []
        string = f.readline()
        try:
            while(len(string)>0):
                newEntity = string.split()
                result.append([int(newEntity[0]),int(newEntity[1])])
                string = f.readline()
            f.close()
            return result
        except IOError as e:
            print('The following error occured '+str(e))
            raise e
        
    def readGrades(self):
        f = open(self.__gradeFile, 'r')        
        result = []
        string = f.readline()
        try:
            while(len(string)>0):
                newEntity = string.split()
                result.append(Grade(int(newEntity[0]),int(newEntity[1]),float(newEntity[2])))
                string = f.readline()
            f.close()
            return result
        except IOError as e:
            print('The following error occured '+str(e))
            raise e
            
class GradeBinaryFileRepository(GradeRepository):
    
    def __init__(self,enrolledFile,gradeFile):
        super().__init__([],[],[],[])
        self.__enrolled = enrolledFile
        self.__grades = gradeFile
        
    def writeToFile(self,enrolled,grades):
        f = open(self.__enrolled,'wb')
        g = open(self.__grades,'wb')
        pickle.dump(enrolled,f)
        pickle.dump(grades,g)
        f.close()
        g.close()
        
    def readEnrolledFromBinary(self):
        try:
            f = open(self.__enrolled, "rb")
            return pickle.load(f)   
        except EOFError:
            return []
        except IOError as e:
            print("The following error occured - " + str(e))
            raise e
        
    def readGradesFromBinary(self):
        try:
            f = open(self.__grades, 'rb')
            return pickle.load(f)
        except EOFError:
            return []
        except IOError as e:
            print('The folloing error occured - ' + str(e))
            raise e
            