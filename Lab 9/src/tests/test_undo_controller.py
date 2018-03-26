'''
Created on Nov 30, 2016

@author: Andreea
'''
import unittest
from src.controller.undo_controller import UndoController
from src.controller.entity_controller import EntityController
from src.controller.grade_controller import GradeController
from src.repository.grade_repository import GradeRepository
from src.repository.entity_repository import EntityRepository
from src.domain.entities import Grade
from src.controller.undo_controller import UndoController
from src.domain.validators import UndoRepositoryException

class TestUndoController(unittest.TestCase):
    
    def setUp(self):
        studs = EntityRepository([(1,'Ratiu Cosmina'),(2,'Kiraly Alex'),(3,'Popa Andra'),(4,'Ocian Eduard'),(5,'Groza Segiu')])
        discs = EntityRepository([(1,'Mate'),(2,'Romana'),(3,'Engleza')])
        self.__studCtrl = EntityController(studs)
        self.__discCtrl = EntityController(discs)
        enrolled = [(1,1),(1,2),(2,2),(2,3),(3,1),(3,3),(4,3),(4,2),(5,1),(5,2)]
        grades = [Grade(1,1,9.8),Grade(1,2,7.5),Grade(2,2,6.8),Grade(2,3,8.8),Grade(3,1,4.5),Grade(3,3,7.3),Grade(4,3,9.6),Grade(4,2,6),Grade(5,1,5.5),Grade(5,2,4.5)]
        self.__grdRepo = GradeRepository(self.__studCtrl.repository,self.__discCtrl.repository,enrolled,grades)
        self.__grdCtrl = GradeController(self.__grdRepo)
        self.__undoController = UndoController()
        self.__undoController.save(self.__studCtrl,self.__discCtrl,self.__grdCtrl)
        unittest.TestCase.setUp(self)
        
    def testSave(self):
        studCtrl = EntityController(EntityRepository([]))
        discCtrl = EntityController(EntityRepository([]))
        repo = GradeRepository(studCtrl.repository,discCtrl.repository,[],[])
        grdCtrl = GradeController(repo)
        self.assertEqual(self.__undoController.save(studCtrl,discCtrl,grdCtrl), (studCtrl,discCtrl,grdCtrl), 'Function save doesn\'t work!')
        
    def testUndo(self):
        studCtrl = EntityController(EntityRepository([]))
        discCtrl = EntityController(EntityRepository([]))
        repo = GradeRepository(studCtrl.repository,discCtrl.repository,[],[])
        grdCtrl = GradeController(repo)
        self.__undoController.save(studCtrl,discCtrl,grdCtrl)
        self.assertEqual(self.__undoController.undo(), (self.__studCtrl,self.__discCtrl,self.__grdCtrl), 'Function undo doesn\'t work!')
         
    def testRedo(self):
        studCtrl = EntityController(EntityRepository([]))
        discCtrl = EntityController(EntityRepository([]))
        repo = GradeRepository(studCtrl.repository,discCtrl.repository,[],[])
        grdCtrl = GradeController(repo)
        self.__undoController.save(studCtrl,discCtrl,grdCtrl)
        self.__undoController.undo()
        self.assertEqual(self.__undoController.redo(), (studCtrl,discCtrl,grdCtrl), 'Function redo doesn\'t work!')
