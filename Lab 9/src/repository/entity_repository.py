'''
Created on Nov 6, 2016

@author: Andreea
'''

from src.domain.validators import RepositoryException
from _collections_abc import Iterable

'''
Universal repository to store a dictionary of entities (students or disciplines)
'''
class EntityRepository(Iterable):
    '''
    Constructor - self._entities will be a dictionary having as key the entity ID and as value its name
    '''
    def __init__(self,l):
        self._entities = {}
        for i in l:
            self._entities[i[0]] = i[1]
            
    def __iter__(self):
        return self
    
    def __next__(self,i):
        return self._entities[i+1]
    
    def __setItem__(self,i,value):
        self._entities[i] = value
        
    def __delItem__(self,i):
        del self._entities[i]
        
    @property
    def entities(self):
        return self._entities
    
    def setEntities(self,l):
        for x in l:
            self._entities[x[0]] = x[1]
        
    def getAll(self):
        return [(x,self._entities[x]) for x in self._entities]
    
    '''
    Returns the name of teh entity with the ID "ID" or None - if the entity is not found in the entity list
    '''
    def findByID(self,ID):
        if not ID in self._entities:
            return None
        return self._entities[ID] 
    
    '''
    Adds entity to the dictionary of {entityID:'entityName'} unless the ID is already taken
    Raises:
    RepositoryException - if ID is already taken
    '''
    def add(self,entity):
        if not self.findByID(entity.ID) is None:
            raise RepositoryException('\nThis ID is already taken!!! Please try adding the student using another ID ...\n')
        self._entities[entity.ID] = entity.name
    
    '''
    Removes the entity having the ID "entityID"
    Raises:
    RepositoryException - if there is no entity with the ID "entityID" in the repository
    '''
    def removeByID(self,entityID):
        if self.findByID(entityID) is None:
            raise RepositoryException('\nID does not exist! Try again ...\n')
        del self._entities[entityID]
    
    '''
    Returns a string representing all the entities from the repository which contain "ID" in their ID
    '''   
    def searchByID(self,ID):
        s = []
        for x in self._entities:
            if str(ID) in str(x):
                s.append((x,self.findByID(x)))
        return s
    
    '''
    Returns a string representing all the entities from the repository which contain "name" in their name
    '''    
    def searchByName(self,name):
        s = []
        for x in self._entities:
            if name.lower() in self._entities[x].lower():
                s.append((x,self.findByID(x)))
        return s
        
    '''
    Updates the entity "entity" with the new name "name"
    '''
    def update(self,entity,name):
        if self.findByID(entity.ID) is None:
            raise RepositoryException('\nID does not exist! Try again ...\n')
        self._entities[entity.ID] = name
    
    '''
    Returns a string representing the list of all entities (ID tab name)
    '''
    def list(self):
        s = []
        for x in self._entities.keys():
            s.append((x,self._entities[x])) 
        return s