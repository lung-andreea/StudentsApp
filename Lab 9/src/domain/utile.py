'''
Created on Jan 7, 2017

@author: Andreea
'''
from _collections_abc import Iterable, generator, Generator


def shellSort(l,comparisonFunction):
    interval = 1
    while interval < len(l)//3:
        interval = interval*3 + 1
    while interval > 0:
        for outer in range (interval, len(l)):
            valueToInsert = l[outer]
            inner = outer
            while inner > interval - 1 and not comparisonFunction(l[inner - interval], valueToInsert):
                l[inner] = l[inner - interval]
                inner = inner - interval
            l[inner] = valueToInsert
        interval = (interval - 1)//3
    return l

def filterMethod(l, acceptanceFunction):
    outputList = []
    for element in l:
        if acceptanceFunction(element):
            outputList.append(element)
    return outputList  
    
