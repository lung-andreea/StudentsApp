'''
Created on Nov 21, 2016

@author: Andreea
'''
import unittest
from src.domain.entities import Entity
from src.repository.entity_repository import EntityRepository
from src.repository.grade_repository import GradeRepository
from src.controller.grade_controller import GradeController
from src.domain.entities import Grade

class TestGradeController(unittest.TestCase):
    
    def setUp(self):
        students = EntityRepository([(1,'Tania Popescu'),(2,'Anca Vlad'),(3,'Bianca Marculescu')])
        disciplines = EntityRepository([(1,'Matematica'),(2,'Romana'),(3,'Engleza')])
        gradeRepo = GradeRepository(students,disciplines,[(1,1),(1,2),(2,2),(2,3),(3,1),(3,3)],[Grade(1,1,9.2),Grade(1,1,6.7),Grade(1,2,10),Grade(1,2,9.4),Grade(2,2,7.8),Grade(3,1,5.6),Grade(3,3,4.5),Grade(3,3,7.7)])
        self.grade_con = GradeController(gradeRepo)
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testEnroll(self):
        self.grade_con.enroll(3,2)
        self.assertEqual(self.grade_con.repository.enrolled, [(1,1),(1,2),(2,2),(2,3),(3,1),(3,3),(3,2)], 'Function enroll doesn\'t work!')
        
    def testAddGrade(self):
        self.grade_con.add(2,3,8.6)
        self.assertEqual(len(self.grade_con.repository.grades),9, 'Function addGrade doesn\'t work!')
        
    def testRemoveGradeByStudentID(self):
        self.grade_con.removeByStudentID(1)
        self.assertEqual(len(self.grade_con.repository.grades),4, 'Function removeGradeByStudentID doesn\'t work!')
        
    def testRemoveGradeByDisciplineID(self):
        self.grade_con.removeByDisciplineID(3)
        self.assertEqual(len(self.grade_con.repository.grades),6, 'Function removeGradeByDisciplineID doesn\'t work!')
        
    def testSortStudsAlpha(self):
        self.assertEqual(self.grade_con.sortStudsAlpha(1), [(3,'Bianca Marculescu'),(1,'Tania Popescu')], 'Function sortStudsAlpha doesn\'t work!')
        
    def testSortStudsDesc(self):
        self.assertEqual(self.grade_con.sortStudsDesc(1), [(1,'Tania Popescu',7.95),(3,'Bianca Marculescu',5.6)], 'Function sortStudsDesc doesn\'t work!')
        
    def testFail(self):
        self.grade_con.add(3, 1, 3)
        self.assertEqual(self.grade_con.fail(), [(3,'Bianca Marculescu')], 'Function fail doesn\'t work!')
        
    def testBest(self):
        self.assertEqual(self.grade_con.best(), [(1,'Tania Popescu',8.82),(2,'Anca Vlad',7.8),(3,'Bianca Marculescu',5.85)], 'Function best doesn\'t work!')
        
    def testTopDisc(self):
        self.assertEqual(self.grade_con.topDisc(), [(2,'Romana',8.75),(1,'Matematica',6.78),(3,'Engleza',6.1)], 'Function topDisc doesn\'t work!')
            
        
    