'''
Created on Nov 5, 2016

@author: Andreea
'''
from copy import deepcopy
from src.domain.validators import InputValidator

from src.UI.read_menu import readCommand
from src.controller.entity_controller import EntityController
from src.controller.grade_controller import GradeController
from src.controller.undo_controller import UndoController
from src.domain.validators import RepositoryException


class Console(object):
    
    def __init__(self,studentController,disciplineController,GradeController): 
        self.__studentController = studentController
        self.__disciplineController = disciplineController
        self.__gradeController = GradeController
        self.__undoController = UndoController()
        self.__inputValidator = InputValidator()
            
    def addUI(self,d):
        ID = input('{0} ID:'.format('Student' if d == 1 else 'Discipline'))
        if not self.__inputValidator.isInteger(ID):
            while not self.__inputValidator.isInteger(ID):
                ID = input('Invalid ID! Try again ...\n>>')
        ID = int(ID)
        name = input('{0} name:'.format('Student' if d == 1 else 'Discipline'))
        if self.__inputValidator.hasNumbers(name):
            while self.__inputValidator.hasNumbers(name):
                name = input('Invalid name! Try again ...\n>>')
        if d == 1: 
            self.__studentController.add(ID,name)
            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])

        else:
            self.__disciplineController.add(ID,name)
            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
            
    def removeUI(self,d):
        ID = input('ID of {0} to be removed:'.format('student' if d == 1 else 'discipline'))
        if not self.__inputValidator.isInteger(ID):
            while not self.__inputValidator.isInteger(ID):
                ID = input('Invalid ID! Try again ...\n>>')
        ID = int(ID)
        if d == 1: 
            self.__studentController.removeByID(ID)
            self.__gradeController.removeByStudentID(ID)
            self.__gradeController.repository.deEnrollStudent(ID)
            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
        else:
            self.__disciplineController.removeByID(ID)
            self.__gradeController.removeByDisciplineID(ID)
            self.__gradeController.repository.deEnrollDiscipline(ID)
            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
            
    def updateUI(self,d):
        ID = input('ID of {0} to be updated:'.format('student' if d == 1 else 'discipline'))
        if not self.__inputValidator.isInteger(ID):
            while not self.__inputValidator.isInteger(ID):
                ID = input('Invalid ID! Try again ...\n>>')
        ID = int(ID)
        name = input('New name for {0}:'.format('student' if d == 1 else 'discipline'))
        if self.__inputValidator.hasNumbers(name):
            while self.__inputValidator.hasNumbers(name):
                name = input('Invalid name! Try again ...\n>>')
        if d == 1: 
            self.__studentController.update(ID,name)
            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
        else:
            self.__disciplineController.update(ID,name)
            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
            
    def listUI(self,d):
        if d == 1: 
            self.__printList2(self.__studentController.list())
        else:
            self.__printList2(self.__disciplineController.list())
    
    def enrollUI(self,stID,discID):
        self.__gradeController.enroll(stID,discID)
        undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
        self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
        
    def gradeUI(self,stID,discID):
        gr = input('Grade:')
        if not self.__inputValidator.isFloat(gr) or float(gr)<1.0 or float(gr)>10.0:
            while not self.__inputValidator.isFloat(gr) or float(gr)<1.0 or float(gr)>10.0:
                gr = input('Invalid grade! Try again ...\n>>')
        gr = float('{:.2f}'.format(float(gr)))
        self.__gradeController.add(stID,discID,gr)
        undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
        self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
        
    def searchDisciplinesUI(self,keyWord):
        if self.__inputValidator.isInteger(keyWord):
            self.__printList2(self.__disciplineController.searchByID(keyWord))
        else:
            self.__printList2(self.__disciplineController.searchByName(keyWord))
        
    def searchStudentsUI(self,keyWord):
        if self.__inputValidator.isInteger(keyWord):
            self.__printList2(self.__studentController.searchByID(keyWord))
        else:
            self.__printList2(self.__studentController.searchByName(keyWord))
            
    def sortUI(self,discID,d):
        if d == 1:
            self.__printList2(self.__gradeController.sortStudsAlpha(discID))
        else:
            self.__printList3(self.__gradeController.sortStudsDesc(discID))
            
    def failUI(self):
        self.__printList2(self.__gradeController.fail())
        
    def bestUI(self):
        self.__printList3(self.__gradeController.best())
        
    def topDiscUI(self):
        self.__printList3(self.__gradeController.topDisc())
    
    def undoUI(self):
        undoList = self.__undoController.undo()
        self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
        
    def redoUI(self):
        redoList = self.__undoController.redo()
        self.__studentController,self.__disciplineController,self.__gradeController =  deepcopy(redoList[0]), deepcopy(redoList[1]), deepcopy(redoList[2]) 
    
    def __printList2(self,l):
        print('')
        for x in l:
            print('{0}\t{1}'.format(x[0],x[1]))
        print('')
        
    def __printList3(self,l):
        print('')
        for x in l:
            print('{0}\t{1}\t{2}'.format(x[0],x[1],x[2]))
        print('')  
          
    def runApp(self):  
        dicts = {1:{1:self.addUI,2:self.removeUI,3:self.updateUI,4:self.listUI},2:{1:self.enrollUI,2:self.gradeUI},3:{1:self.searchDisciplinesUI,2:self.searchStudentsUI},4:{1:self.sortUI,2:self.failUI,3:self.bestUI,4:self.topDiscUI},5:{1:self.undoUI,2:self.redoUI}}
        self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
        while True:
            try:
                cmd = readCommand()
                if cmd == 'exit':
                    break
                dicts[cmd[0]][cmd[1]](*cmd[2:])
            except ValueError as ve:
                print(ve)
            except RepositoryException as exe:
                print(exe)