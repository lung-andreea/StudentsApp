'''
Created on Dec 11, 2016

@author: Andreea
'''
import pickle

from src.repository.entity_repository import EntityRepository


class EntityFileRepository(EntityRepository):

    def __init__(self, fileName):
        super().__init__([])
        self.__file = fileName
        
    def writeToFile(self):
        f = open(self.__file,'w')
        try:
            for x in self._entities:
                string = str(x)+' '+self._entities[x]+'\n'
                f.write(string)
            f.close()
        except Exception as e:
            print('The following error occured '+str(e))
            
    def readFromFile(self):
        result = []
        f = open(self.__file, 'r')
        string = f.readline()
        try:
            while(len(string)>0):
                newEntity = string.split()
                s = ''
                for i in newEntity[1:]:
                    s+= ' '+i
                result.append([int(newEntity[0]),s])
                string = f.readline()
            f.close()
            return result
        except IOError as e:
            print('The following error occured '+str(e))
            raise e
        
    def add(self, entity):
        EntityRepository.add(self, entity)
        self.writeToFile()
      
    def removeByID(self, entityID):
        EntityRepository.removeByID(self, entityID)
        self.writeToFile()
          
    def update(self, entity, name):
        EntityRepository.update(self, entity, name)
        self.writeToFile()  
    
    
class EntityBinaryFileRepository(EntityRepository):
    
    def __init__(self, fileName):
        super().__init__([])
        self.__fileName = fileName
        
    def writeToFile(self):
        f = open(self.__fileName, "wb")
        pickle.dump(self._entities, f)
        f.close()
        
    def readBinaryFile(self):
        try:
            f = open(self.__fileName, "rb")
            l = pickle.load(f)
            return [(x,l[x]) for x in l]  
        except EOFError:
            return []
        except IOError as e:
            print("The following error occured - " + str(e))
            raise e

    def add(self, entity):
        EntityRepository.add(self, entity)
        self.writeToFile()
        
    def removeByID(self, entityID):
        EntityRepository.removeByID(self, entityID)
        self.writeToFile()
        
    def update(self, entity, name):
        EntityRepository.update(self, entity, name)
        self.writeToFile()
    
