'''
Created on Nov 20, 2016

@author: Andreea
'''
import unittest

from src.domain.entities import Entity
from src.repository.entity_repository import EntityRepository
from src.repository.grade_repository import GradeRepository
from src.domain.validators import RepositoryException
from src.domain.entities import Grade


class TestGradeRepository(unittest.TestCase):
    
    def setUp(self):
        students = EntityRepository([(1,'Tania Popescu'),(2,'Anca Vlad'),(3,'Bianca Marculescu')])
        disciplines = EntityRepository([(1,'Matematica'),(2,'Romana'),(3,'Engleza')])
        self.grade_repo = GradeRepository(students,disciplines,[(1,1),(1,2),(2,2),(2,3),(3,1),(3,3)],[Grade(1,1,9.2),Grade(1,1,6.7),Grade(1,2,10),Grade(1,2,9.4),Grade(2,2,7.8),Grade(3,1,5.6),Grade(3,3,4.5),Grade(3,3,7.7)])
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testIsEnrolled(self):
        self.assertEqual(self.grade_repo.isEnrolled(1, 1), True, 'Function isEnrolled doesn\'t work!')
        self.assertEqual(self.grade_repo.isEnrolled(3, 2), False, 'Function isEnrolled doesn\'t work!')
        
    def testEnroll(self):
        self.grade_repo.enroll(3,2)
        self.assertEqual(self.grade_repo.enrolled, [(1,1),(1,2),(2,2),(2,3),(3,1),(3,3),(3,2)], 'Function enroll doesn\'t work!')
        try:
            self.grade_repo.enroll(4,1)
            assert False
        except RepositoryException:
            pass
        try:
            self.grade_repo.enroll(2,5)
            assert False
        except RepositoryException:
            pass
        try:
            self.grade_repo.enroll(1,1)
            assert False
        except RepositoryException:
            pass
        
    def testAddGrade(self):
        self.grade_repo.addGrade(2,3,8.6)
        self.assertEqual(len(self.grade_repo.grades),9, 'Function addGrade doesn\'t work!')
        try:
            self.grade_repo.addGrade(4,1,9.8)
            assert False
        except RepositoryException:
            pass
        try:
            self.grade_repo.addGrade(2,5,5.6)
            assert False
        except RepositoryException:
            pass
        try:
            self.grade_repo.addGrade(3,2,6)
            assert False
        except RepositoryException:
            pass
        
    def testRemoveGradeByStudentID(self):
        self.grade_repo.removeGradeByStudentID(1)
        self.assertEqual(len(self.grade_repo.grades),4, 'Function removeGradeByStudentID doesn\'t work!')
        
    def testRemoveGradeByDisciplineID(self):
        self.grade_repo.removeGradeByDisciplineID(3)
        self.assertEqual(len(self.grade_repo.grades),6, 'Function removeGradeByDisciplineID doesn\'t work!')
        
    def testSortStudsAlpha(self):
        self.assertEqual(self.grade_repo.sortStudsAlpha(1), [(3,'Bianca Marculescu'),(1,'Tania Popescu')], 'Function sortStudsAlpha doesn\'t work!')
        
    def testSortStudsDesc(self):
        self.assertEqual(self.grade_repo.sortStudsDesc(1), [(1,'Tania Popescu',7.95),(3,'Bianca Marculescu',5.6)], 'Function sortStudsDesc doesn\'t work!')
        
    def testFail(self):
        self.grade_repo.addGrade(3, 1, 3)
        self.assertEqual(self.grade_repo.fail(), [(3,'Bianca Marculescu')], 'Function fail doesn\'t work!')
        
    def testBest(self):
        self.assertEqual(self.grade_repo.best(), [(1,'Tania Popescu',8.82),(2,'Anca Vlad',7.8),(3,'Bianca Marculescu',5.85)], 'Function best doesn\'t work!')
        
    def testTopDisc(self):
        self.assertEqual(self.grade_repo.topDisc(), [(2,'Romana',8.75),(1,'Matematica',6.78),(3,'Engleza',6.1)], 'Function topDisc doesn\'t work!')
            
    def testListOfStudEnrolledAt(self):
        self.assertEqual(self.grade_repo.listOfStudEnrolledAt(1), [1,3], 'Function listOfStudEnrolledAt doesn\'t work!')
        
    def testListOfDisciplinesStudentIsEnrolledAt(self):
        self.assertEqual(self.grade_repo.listOfDisciplinesStudentIsEnrolledAt(1), [1,2], 'Function listOfDisciplinesStudentIsEnrolledAt doesn\'t work!')
        
    def testAvg(self):
        self.assertEqual(self.grade_repo.avg(1, 1), 7.95, 'Function avg doesn\'t work!')
        
    def testTotalAvg(self):
        self.assertEqual(self.grade_repo.totalAvg(1), 8.82, 'Function totalAvg doesn\'t work!')
        
    def testAvgByDisciplineID(self):
        self.assertEqual(self.grade_repo.avgByDisciplineID(3), 6.1, 'Function avgByDisciplineID doesn\'t work!')