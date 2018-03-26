'''
Created on Nov 21, 2016

@author: Andreea
'''
import unittest
from src.controller.entity_controller import EntityController
from src.repository.entity_repository import EntityRepository

class TestEntityController(unittest.TestCase):
    
    def setUp(self):
        repo = EntityRepository([(1,'Tania Popescu'),(2,'Anca Vlad'),(3,'Bianca Marculescu')])
        self.entity_con = EntityController(repo)
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testAdd(self):
        self.entity_con.add(4,'Maria Ioana')
        self.assertEqual(self.entity_con.repository.entities[4], 'Maria Ioana', 'Add function doesn\'t work!')
        
    def testRemoveByID(self):
        self.entity_con.removeByID(3)
        self.assertEqual(len(self.entity_con.repository.entities), 2, 'Function remove doesn\'t work!')
    
    def testSearchByID(self):
        self.assertEqual(self.entity_con.searchByID(1), [(1,'Tania Popescu')], 'Function searchByID doesn\'t work!')
        
    def testSearchByName(self):
        self.assertEqual(self.entity_con.searchByName('anc'), [(2,'Anca Vlad'),(3,'Bianca Marculescu')], 'Function searchByID doesn\'t work!')
        
    def testUpdate(self):
        self.entity_con.update(1, 'Miruna Matei')
        self.assertEqual(self.entity_con.repository.entities[1], 'Miruna Matei', 'Function update doesn\'t work!')
        
    def testList(self):
        self.assertEqual(self.entity_con.list(), [(1,'Tania Popescu'),(2,'Anca Vlad'),(3,'Bianca Marculescu')], 'Function list doesn\'t work!')