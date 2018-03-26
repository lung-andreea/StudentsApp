'''
Created on Nov 20, 2016

@author: Andreea
'''
import unittest
from src.repository.entity_repository import EntityRepository
from src.domain.entities import Entity
from src.domain.validators import RepositoryException

class TestEntityRepository(unittest.TestCase):
    
    def setUp(self):
        self.entity_repo = EntityRepository([(1,'Tania Popescu'),(2,'Anca Vlad'),(3,'Bianca Marculescu')])
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testAdd(self):
        entity = Entity(4,'Maria Ioana')
        self.entity_repo.add(entity)
        self.assertEqual(self.entity_repo.entities[4], 'Maria Ioana', 'Add function doesn\'t work!')
        try:
            self.entity_repo.add(Entity(1,'Alex Pop'))
            assert False
        except RepositoryException:
            pass
        
    def testRemoveByID(self):
        self.entity_repo.removeByID(3)
        self.assertEqual(len(self.entity_repo.entities), 2, 'Function remove doesn\'t work!')
        try:
            self.entity_repo.removeByID(4)
            assert False
        except RepositoryException:
            pass
        
    def testFindByID(self):
        self.assertEqual(self.entity_repo.findByID(1), 'Tania Popescu', 'Function findByID doesn\'t work!')
        self.assertEqual(self.entity_repo.findByID(4), None, 'Function findByID doesn\'t work!')
    
    def testSearchByID(self):
        self.assertEqual(self.entity_repo.searchByID(1), [(1,'Tania Popescu')], 'Function searchByID doesn\'t work!')
        self.assertEqual(self.entity_repo.searchByID(4), [], 'Function searchByID doesn\'t work!')
        
    def testSearchByName(self):
        self.assertEqual(self.entity_repo.searchByName('anc'), [(2,'Anca Vlad'),(3,'Bianca Marculescu')], 'Function searchByID doesn\'t work!')
        self.assertEqual(self.entity_repo.searchByID('cartof'), [], 'Function searchByID doesn\'t work!')
         
    def testUpdate(self):
        entity = Entity(1,'Tania Popescu')
        self.entity_repo.update(entity, 'Miruna Matei')
        self.assertEqual(self.entity_repo.entities[1], 'Miruna Matei', 'Function update doesn\'t work!')
        try:
            self.entity_repo.update(Entity(4,'Dragos Andrei'), 'Otilia Marculescu')
            assert False
        except RepositoryException:
            pass
         
    def testList(self):
        self.assertEqual(self.entity_repo.list(), [(1,'Tania Popescu'),(2,'Anca Vlad'),(3,'Bianca Marculescu')], 'Function list doesn\'t work!')
