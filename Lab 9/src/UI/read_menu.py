'''
Created on Nov 4, 2016

@author: Andreea
'''
from src.domain.validators import InputValidator

def read1():
    print('1 - add / 2 - remove / 3 - update / 4 - list')
    while True:
        try:
            c = int(input('>>'))
            if not c in {1,2,3,4}:
                raise ValueError
            break
        except ValueError:
            print('Invalid command! Try again ...')
    print('1 - Students / 2 - Disciplines')
    while True:
        try:
            d = int(input('>>'))
            if not d in {1,2}:
                raise ValueError
            break
        except ValueError:
            print('Invalid command! Try again ...')    
    return [c,d]

def read2():
    inputValidator = InputValidator()
    print('1 - enroll / 2 - grade')
    while True:
        try:
            c = int(input('>>'))
            if not c in {1,2}:
                raise ValueError
            break
        except ValueError:
            print('Invalid command! Try again ...')
    d = input('Student ID:')
    if not inputValidator.isInteger(d):
        while not inputValidator.isInteger(d):
                d = input('Invalid student ID! Try again\n>>')
    d = int(d)
    e = input('Discipline ID:')
    if not inputValidator.isInteger(e):
        while not inputValidator.isInteger(e):
                e = input('Invalid discipline ID! Try again\n>>')
    e = int(e)
    return [c,d,e]


def read3():
    inputValidator = InputValidator()
    print('1 - Disciplines / 2 - Students')
    while True:
        try:
            c = int(input('>>'))
            if not c in {1,2}:
                raise ValueError
            break
        except ValueError:
            print('Invalid command! Try again ...')
    keyWord = input('ID/name:')
    if not inputValidator.isInteger(keyWord):
        if inputValidator.hasNumbers(keyWord):
            raise ValueError('You should either search by ID or name, not by both ...')
    else:
        keyWord = int(keyWord)
    return [c,keyWord]
    
def read4():
    inputValidator = InputValidator()
    print('1 - sort students at a given discipline\n2 - show failing students (at one or more disciplines)\n3 - show students with the best school situation\n4 - show disciplines sorted descending by average grade')
    while True:
        try:
            c = int(input('>>'))
            if not c in {1,2,3,4}:
                raise ValueError
            break
        except ValueError:
            print('Invalid command! Try again ...')
    if not c == 1:
        return [c]
    else:
        discID = input('Discipline ID:')
        if not inputValidator.isInteger(discID):
            while not inputValidator.isInteger(discID):
                discID = input('Invalid discipline ID! Try again ...\n>>')
        discID = int(discID)
        print('1 - Alphabetically / 2 - Descending by average grade')
        while True:
            try:
                d = int(input('>>'))
                if not d in {1,2}:
                    raise ValueError
                break
            except ValueError:
                print('Invalid command! Try again ...')
        return [c,discID,d]
            
def read5():
    print('1 - Undo / 2 - Redo')
    while True:
        try:
            d = int(input('>>'))
            if not d in {1,2}:
                raise ValueError
            break
        except ValueError:
            print('Invalid command! Try again ...')
    return [d]

def exitProg():
    return None
    
def readCommand():
    features = {1:read1,2:read2,3:read3,4:read4,5:read5,6:exitProg}
    print('1 - add/remove/update/list: students/disciplines\n2 - enroll/grade student at discipline\n3 - search for disciplines/students by ID/name\n4 - view statistics\n5 - undo/redo\n6 - exit\n')
    while True:
        try:
            c = int(input('>>'))
            if not c in {1,2,3,4,5,6}:
                raise ValueError
            break
        except ValueError:
            print('There\'s no such feature! Try again ...')
    if c == 6:
        return 'exit'
    return [c, *features[c]()]
    
