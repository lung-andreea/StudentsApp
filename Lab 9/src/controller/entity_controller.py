'''
Created on Nov 5, 2016

@author: Andreea
'''
'''
Class performs the operations implying entities:
Arguments:
repository - where the entities are stored
'''

from src.domain.entities import Entity

class EntityController(object):
    def __init__(self, repository):
        self.__repository = repository
        
    @property
    def repository(self):
        return self.__repository
        
    '''
    Adds entity having the ID "ID" and name "name" to the list of entities
    '''
    def add(self,ID,name):
        entity = Entity(ID,name)
        self.__repository.add(entity)
    
    '''
    Removes entity with the ID "entityID" from the entities list
    '''
    def removeByID(self,entityID):
        self.__repository.removeByID(entityID)
        
    '''
    Returns a string representing all the entities from the repository which contain "entityID" in their ID
    '''
    def searchByID(self,entityID):
        return self.__repository.searchByID(entityID)
        
    '''
    Returns a string representing all the entities from the repository which contain "entityName" in their name
    '''
    def searchByName(self,entityName):
        return self.__repository.searchByName(entityName)
    
    '''
    Changes the name of the entity having the ID "ID" to the new name "name"
    '''
    def update(self,ID,name):
        entity = Entity(ID,self.__repository.findByID(ID))
        self.__repository.update(entity,name)
    
    '''
    Returns a string representing the list of all entities (ID tab name)
    '''
    def list(self):
        return self.__repository.list()
