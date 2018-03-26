'''
Created on Dec 1, 2016
   
@author: Andreea
'''
from tkinter import *
from src.domain.validators import InputValidator
from src.controller.undo_controller import UndoController
from copy import deepcopy
from src.domain.validators import RepositoryException
    
class GUI(object):
    def __init__(self,studentController,disciplineController,gradeController):
        self.__studentController = studentController
        self.__disciplineController = disciplineController
        self.__gradeController = gradeController
        self.__undoController = UndoController()
        self.__inputValidator = InputValidator()
        
        self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
        self.tk = Tk()
        self.tk.title('Students Register Management')
        frameLft = Frame(self.tk)
        self.frameRgt = Frame(self.tk)
        self.listAll = Label(self.frameRgt, width = 30)
        self.listAll.pack(expand = YES)
        frameLft.pack(side = LEFT)
        self.frameRgt.pack(side = LEFT)
        self.errorLabel = Label(frameLft)
        self.frame1 = Frame(frameLft)
        self.frame2 = Frame(frameLft)
        self.frame3 = Frame(frameLft)
        self.frame4 = Frame(frameLft)
        self.frame5 = Frame(frameLft)
        br1 = Label(frameLft)
        br2 = Label(frameLft)
        br3 = Label(frameLft)
        br4 = Label(frameLft)
        br5 = Label(frameLft)
        br6 = Label(frameLft)
        br6.pack()
        self.frame1.pack(fill = X)
        br1.pack()
        self.frame2.pack(fill = X)
        br2.pack()
        self.frame3.pack(fill = X)
        br3.pack()
        self.frame4.pack(fill = X)
        br4.pack()
        self.frame5.pack(fill = X)
        br5.pack()
        self.errorLabel.pack()    
        self.add = Button(self.frame1, text = 'Add', width = 6)
        self.add.bind('<Button-1>',self.addGUI)
        self.remove = Button(self.frame1, text = 'Remove', width = 6)
        self.remove.bind('<Button-1>',self.removeGUI)
        self.update = Button(self.frame1, text = 'Update', width = 6)
        self.update.bind('<Button-1>',self.updateGUI)
        self.list = Button(self.frame1, text = 'list', width = 6)
        self.list.bind('<Button-1>',self.listGUI)
        self.packframe1()
        self.studdiscLbl = Label(self.frame1)
        self.students1  = Button(self.studdiscLbl, text = 'Students')
        self.disciplines1 = Button(self.studdiscLbl, text = 'Disciplines')
        self.students1.pack(side = LEFT)
        self.disciplines1.pack(side = LEFT)
        
        self.enrollgradeLbl = Label(self.frame2)     
        self.enroll = Button(self.enrollgradeLbl, text = 'Enroll', width = 6)
        self.enroll.bind('<Button-1>',self.enrollGUI)
        self.enroll.pack(side = LEFT)
        self.grade = Button(self.enrollgradeLbl, text = 'Grade', width = 6)
        self.grade.bind('<Button-1>',self.gradeGUI)
        self.grade.pack(side = LEFT)
        self.packframe2()
        self.enrollgradeLbl.pack(expand = YES)
        
        self.srchLbl = Label(self.frame3) 
        self.srchLbl.pack(expand = YES)    
        self.searchLbl = Label(self.srchLbl, text = 'Search for: ')
        self.searchLbl.pack(side = LEFT)
        self.disciplines2 = Button(self.srchLbl, text = 'Disciplines')
        self.disciplines2.bind('<Button-1>',self.searchDisciplinesGUI)
        self.disciplines2.pack(side = LEFT)
        self.students2 = Button(self.srchLbl, text = 'Students') 
        self.students2.bind('<Button-1>',self.searchStudentsGUI)
        self.students2.pack(side = LEFT)
        self.packframe3()
             
        self.frameSort = Frame(self.frame4)
        self.stat1 = Button(self.frameSort, text = 'Sort students at a given discipline')
        self.stat1.bind('<Button-1>',self.sortGUI)
        self.stat2 = Button(self.frame4, text = 'Show failing students')
        self.stat2.bind('<Button-1>',self.failGUI)
        self.stat3 = Button(self.frame4, text = 'Show students with the best school situation')
        self.stat3.bind('<Button-1>',self.bestGUI)
        self.stat4 = Button(self.frame4, text = 'Show disciplines sorted descending by average grade')
        self.stat4.bind('<Button-1>',self.topDiscGUI)
        self.frameSort.pack(fill = X)
        self.stat1.pack(fill = X)
        self.stat2.pack(fill = X)
        self.stat3.pack(fill = X)
        self.stat4.pack(fill = X)
        
        undoRedoLbl = Label(self.frame5)     
        self.undo = Button(undoRedoLbl, text = 'Undo', width = 6)
        self.undo.bind('<Button-1>',self.undoGUI)
        self.redo = Button(undoRedoLbl, text = 'Redo', width = 6)
        self.redo.bind('<Button-1>',self.redoGUI)
        self.undo.pack(side = LEFT)
        self.redo.pack(side = LEFT)
        undoRedoLbl.pack(expand = YES)
             
    def startGUI(self):  
        self.tk.mainloop()
        
    def clearframe1(self):
        self.add.pack_forget()
        self.remove.pack_forget()
        self.update.pack_forget()
        self.list.pack_forget()
        self.studdiscLbl.pack(expand = YES)
          
    def packframe1(self):
        self.add.pack(side = LEFT,expand = YES)
        self.remove.pack(side = LEFT,expand = YES)
        self.update.pack(side = LEFT, expand = YES)
        self.list.pack(side = LEFT, expand = YES)
     
    def clearframe2(self):    
        self.enrollgradeLbl.pack_forget()
        
    def packframe2(self):
        self.enrollgradeLbl.pack()
        
    def clearframe3(self):
        self.srchLbl.pack_forget()
        
    def packframe3(self):
        self.srchLbl.pack()
                   
    def addGUI(self,event):
        def performAdd(i):
            def ok(event):
                ID = IDvar.get()
                IDvar.set('')
                name = nameVar.get()
                nameVar.set('')
                if not self.__inputValidator.isInteger(ID) or self.__inputValidator.hasNumbers(name):
                        again()
                else:
                    if i == 'Student':
                        try:
                            self.__studentController.add(int(ID),name)
                            self.errorLabel.configure(text = '')
                            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
                            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
                            resetframe()
                        except RepositoryException as ex:
                            self.errorLabel.configure(text = ex)
                    else:
                        try:
                            self.__disciplineController.add(int(ID),name) 
                            self.errorLabel.configure(text = '')
                            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
                            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
                            resetframe()
                        except RepositoryException as ex:
                            self.errorLabel.configure(text = ex)
                           
            def again():
                errorLbl.pack(side = BOTTOM)
           
            def resetframe():
                def clearframe():
                    errorLbl.pack_forget()
                    idLbl.pack_forget()
                    IDent.pack_forget()
                    nameLbl.pack_forget()
                    nameEnt.pack_forget()
                    OK.pack_forget()
                clearframe()
                self.packframe1()
                
            if i == 1:
                i = 'Student'
            else:
                i = 'Discipline'
            self.studdiscLbl.pack_forget()
            IDvar = StringVar()
            nameVar = StringVar()
            idLbl = Label(self.frame1, text = i+' ID: ')
            nameLbl = Label(self.frame1, text = i+' name: ')
            IDent = Entry(self.frame1, textvariable = IDvar)
            nameEnt = Entry(self.frame1, textvariable = nameVar)
            OK = Button(self.frame1, text = 'OK')
            OK.bind('<Button-1>',ok)
            idLbl.pack(side = LEFT)
            IDent.pack(side = LEFT)
            nameLbl.pack(side = LEFT)
            nameEnt.pack(side = LEFT)
            OK.pack(side = LEFT)  
        self.clearframe1()
        self.studdiscLbl.pack(expand = YES)
        self.students1.configure(command = lambda:performAdd(1))
        self.disciplines1.configure(command = lambda:performAdd(2))
        errorLbl = Label(self.frame1, text = 'Invalid input! Try again ...')
                    
    def removeGUI(self,event):
        def performRemove(i):
            def ok(event):
                ID = IDvar.get()
                IDvar.set('')
                if not self.__inputValidator.isInteger(ID):
                    again()
                else:
                    ID = int(ID)
                    if i == 'student': 
                        try:   
                            self.errorLabel.configure(text = '')
                            self.__studentController.removeByID(ID)
                            self.__gradeController.removeByStudentID(ID)
                            self.__gradeController.repository.deEnrollStudent(ID)
                            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
                            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
                            resetframe()
                        except RepositoryException as ex:
                            self.errorLabel.configure(text = ex)
                    else:
                        try:   
                            self.errorLabel.configure(text = '')
                            self.__disciplineController.removeByID(ID)
                            self.__gradeController.removeByDisciplineID(ID)
                            self.__gradeController.repository.deEnrollDiscipline(ID)
                            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
                            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
                            resetframe() 
                        except RepositoryException as ex:
                            self.errorLabel.configure(text = ex)
                        
            def again():
                errorLbl.pack(side = BOTTOM)  
                      
            def resetframe():
                def clearframe():
                    errorLbl.pack_forget()
                    lbl.pack_forget()
                    ent.pack_forget()
                    OK.pack_forget()
                clearframe()
                self.packframe1()        
            if i == 1:
                i = 'student'
            else:
                i = 'discipline'
            self.studdiscLbl.pack_forget()
            lbl = Label(self.frame1, text ='ID of '+i+' to be removed: ')
            IDvar = StringVar()
            ent = Entry(self.frame1, textvariable = IDvar)
            OK = Button(self.frame1,text = 'OK')
            OK.bind('<Button-1>',ok)
            lbl.pack(side = LEFT)
            ent.pack(side = LEFT)
            OK.pack(side = LEFT)
        self.clearframe1()
        self.studdiscLbl.pack(expand = YES)
        self.students1.configure(command = lambda: performRemove(1))
        self.disciplines1.configure(command = lambda: performRemove(2))
        errorLbl = Label(self.frame1, text = 'Invalid ID! Try again ...')           
                      
    def updateGUI(self,event): 
        def performUpdate(i):
            def ok(event):
                ID = IDvar.get()
                IDvar.set('')
                name = nameVar.get()
                nameVar.set('')
                if not self.__inputValidator.isInteger(ID) or self.__inputValidator.hasNumbers(name):
                    again() 
                else:
                    if i == 'student':
                        try:   
                            self.errorLabel.configure(text = '')
                            self.__studentController.update(int(ID),name)
                            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
                            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
                            resetframe() 
                        except RepositoryException as ex:
                            self.errorLabel.configure(text = ex) 
                    else:
                        try:   
                            self.errorLabel.configure(text = '')
                            self.__disciplineController.update(int(ID),name)
                            undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
                            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
                            resetframe() 
                        except RepositoryException as ex:
                            self.errorLabel.configure(text = ex)
                        
                        
            def again():
                errorLbl.pack(side = BOTTOM)  
                      
            def resetframe():
                def clearframe():
                    errorLbl.pack_forget()
                    IDlbl.pack_forget()
                    IDent.pack_forget()
                    nameLbl.pack_forget()
                    nameEnt.pack_forget()
                    OK.pack_forget()
                clearframe()
                self.packframe1()    
            if i == 1:
                i = 'student'
            else:
                i = 'discipline'
            self.studdiscLbl.pack_forget()
            IDlbl = Label(self.frame1, text = 'ID of '+i+' to be updated: ')
            nameLbl = Label(self.frame1, text = 'New name for '+i+': ')
            IDvar = StringVar()
            IDent = Entry(self.frame1, textvariable = IDvar)
            nameVar = StringVar()
            nameEnt = Entry(self.frame1, textvariable = nameVar)
            OK = Button(self.frame1,text = 'OK')
            OK.bind('<Button-1>',ok)
            IDlbl.pack()
            IDent.pack()
            nameLbl.pack()
            nameEnt.pack()
            OK.pack()
        self.clearframe1()
        self.studdiscLbl.pack(expand = YES)
        self.students1.configure(command = lambda: performUpdate(1))
        self.disciplines1.configure(command = lambda: performUpdate(2))
        errorLbl = Label(self.frame1, text = 'Invalid input! Try again ...')
                    
    def listGUI(self,event):
        def printStuds():
            self.studdiscLbl.pack_forget()
            self.packframe1()
            self.__printList2(self.__studentController.list())
        def printDiscs():
            self.studdiscLbl.pack_forget()
            self.packframe1()
            self.__printList2(self.__disciplineController.list())
        self.clearframe1()
        self.studdiscLbl.pack(expand = YES)
        self.students1.configure(command = printStuds)
        self.disciplines1.configure(command = printDiscs)
                
    def __printList2(self,l):
        s = '\n'
        for x in l:
            s+= '{0}\t{1}\n'.format(x[0],x[1])
        self.listAll.configure(text = s)
            
    def __printList3(self,l):
        s = '\n'
        for x in l:
            s+= '{0}\t{1}\t{2}\n'.format(x[0],x[1],x[2])
        self.listAll.configure(text = s)
        
    def enrollGUI(self,event):
        def ok(event):
            def again():
                errorLbl.pack(side = BOTTOM)  
                      
            def resetframe():
                def clearframe():
                    errorLbl.pack_forget()
                    lbl1.pack_forget()
                    ent1.pack_forget()
                    lbl2.pack_forget()
                    ent2.pack_forget()
                    OK.pack_forget()
                clearframe()
                self.packframe2()
            studentID = studID.get()
            studID.set('')
            disciplineID = discID.get()
            discID.set('')
            if not self.__inputValidator.isInteger(str(studentID)) or not self.__inputValidator.isInteger(str(disciplineID)):
                again()
            else:
                try:   
                    self.errorLabel.configure(text = '')
                    self.__gradeController.enroll(int(str(studentID)),int(str(disciplineID)))
                    undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
                    self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
                    resetframe()         
                except RepositoryException as ex:
                    self.errorLabel.configure(text = ex)
        self.clearframe2()
        lbl1 = Label(self.frame2, text = 'Student ID: ')
        studID = StringVar()
        ent1 = Entry(self.frame2, textvariable = studID)
        lbl2 = Label(self.frame2, text = 'Discipline ID: ')
        discID = StringVar()
        ent2 = Entry(self.frame2, textvariable = discID)
        OK = Button(self.frame2, text = 'OK')
        OK.bind('<Button-1>',ok)
        errorLbl = Label(self.frame2, text = 'Invalid ID! Try again ...')
        for i in [lbl1,ent1,lbl2,ent2,OK]:
            i.pack(side = LEFT)
        
    def gradeGUI(self,event):
        def ok(event):
            def again():
                errorLbl.pack(side = BOTTOM)  
                      
            def resetframe():
                def clearframe():
                    errorLbl.pack_forget()
                    lbl1.pack_forget()
                    ent1.pack_forget()
                    lbl2.pack_forget()
                    ent2.pack_forget()
                    lbl3.pack_forget()
                    ent3.pack_forget()
                    OK.pack_forget()
                clearframe()
                self.packframe2()   
            studentID = studID.get()
            studID.set('')
            disciplineID = discID.get()
            discID.set('')
            value = val.get()
            val.set('')
            if not self.__inputValidator.isInteger(str(studentID)) or not self.__inputValidator.isInteger(str(disciplineID)) or not self.__inputValidator.isFloat(str(value)) or float(str(value))<1.0 or float(str(value))>10.0:
                again()
            else:
                try:   
                    self.errorLabel.configure(text = '')
                    gr = float('{:.2f}'.format(float(str(value))))
                    self.__gradeController.add(int(str(studentID)),int(str(disciplineID)),gr)
                    undoList = self.__undoController.save(deepcopy(self.__studentController),deepcopy(self.__disciplineController),deepcopy(self.__gradeController))
                    self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])
                    resetframe()         
                except RepositoryException as ex:
                    self.errorLabel.configure(text = ex)
            
        self.clearframe2()
        lbl1 = Label(self.frame2, text = 'Student ID: ')
        studID = StringVar()
        ent1 = Entry(self.frame2, textvariable = studID)
        lbl2 = Label(self.frame2, text = 'Discipline ID: ')
        discID = StringVar()
        ent2 = Entry(self.frame2, textvariable = discID)
        lbl3 = Label(self.frame2, text = 'Value: ')
        val = StringVar()
        ent3 = Entry(self.frame2, textvariable = val)
        OK = Button(self.frame2, text = 'OK')
        OK.bind('<Button-1>',ok)
        errorLbl = Label(self.frame2, text = 'Invalid ID! Try again ...')
        for i in [lbl1,ent1,lbl2,ent2,lbl3,ent3,OK]:
            i.pack(side = LEFT)
     
    def searchDisciplinesGUI(self,event):
        searchit = Button(self.frame3, text = 'Search')
        def again():
                errorLbl.pack(side = BOTTOM)  
                      
        def resetframe():
            def clearframe():
                errorLbl.pack_forget()
                lbl.pack_forget()
                ent.pack_forget()
                searchit.pack_forget()
            clearframe()
            self.packframe3()
              
        def search(event):
            keyWord = keyWordVar.get()
            keyWordVar.set('')
            if not self.__inputValidator.isInteger(keyWord):
                if self.__inputValidator.hasNumbers(keyWord):
                    again()
                else:
                    self.__printList2(self.__disciplineController.searchByName(keyWord))
                    resetframe()
            else:
                self.__printList2(self.__disciplineController.searchByID(keyWord))
                resetframe()
        self.clearframe3()
        lbl = Label(self.frame3, text = 'ID/name: ')
        keyWordVar = StringVar()
        ent = Entry(self.frame3, textvariable = keyWordVar)
        searchit.bind('<Button-1>', search)
        lbl.pack(side = LEFT)
        ent.pack(side = LEFT)
        searchit.pack(side = LEFT)
        errorLbl = Label(self.frame3, text = 'Invalid ID or name! Try again ...')
        
    def searchStudentsGUI(self,event):
        searchit = Button(self.frame3, text = 'Search')
        def again():        
                errorLbl.pack(side = BOTTOM)  
                      
        def resetframe():
            def clearframe():
                errorLbl.pack_forget()
                lbl.pack_forget()
                ent.pack_forget()
                searchit.pack_forget()
            clearframe()
            self.packframe3()  
        
        def search(event):
            keyWord = keyWordVar.get()
            keyWordVar.set('')
            if not self.__inputValidator.isInteger(keyWord):
                if self.__inputValidator.hasNumbers(keyWord):
                    again()
                else:
                    self.__printList2(self.__studentController.searchByName(keyWord))
                    resetframe()
            else:
                self.__printList2(self.__studentController.searchByID(keyWord))
                resetframe()
        self.clearframe3()        
        lbl = Label(self.frame3, text = 'ID/name: ')
        keyWordVar = StringVar()
        ent = Entry(self.frame3, textvariable = keyWordVar)
        searchit.bind('<Button-1>', search)
        lbl.pack(side = LEFT)
        ent.pack(side = LEFT)
        searchit.pack(side = LEFT)
        errorLbl = Label(self.frame3, text = 'Invalid ID or name! Try again ...')
        
    def sortGUI(self,event):
            def sortStudsAlpha(event):
                discID = disciplineID.get()
                disciplineID.set('')
                if not self.__inputValidator.isInteger(discID):
                    again()
                else:
                    try:   
                        self.errorLabel.configure(text = '')
                        discID = int(str(discID))
                        self.__printList2(self.__gradeController.sortStudsAlpha(discID))
                        resetframe()     
                    except RepositoryException as ex:
                        self.errorLabel.configure(text = ex)
            
            def sortStudsDesc(event):
                discID = disciplineID.get()
                disciplineID.set('')
                if not self.__inputValidator.isInteger(discID):
                    again()
                else:
                    try:   
                        self.errorLabel.configure(text = '')
                        discID = int(str(discID))
                        self.__printList3(self.__gradeController.sortStudsDesc(discID))
                        resetframe()      
                    except RepositoryException as ex:
                        self.errorLabel.configure(text = ex)
                              
            def again():
                    errorLbl.pack(side = BOTTOM)  
                      
            def resetframe():
                def clearframe():
                    errorLbl.pack_forget()
                    lbl.pack_forget()
                    ent.pack_forget()
                    alpha.pack_forget()
                    desc.pack_forget()
                clearframe()
                self.stat1.pack()  
                    
            self.stat1.pack_forget()
            lbl = Label(self.frameSort, text = 'Discipline ID: ')
            disciplineID = StringVar()
            ent = Entry(self.frameSort, textvariable = disciplineID)
            alpha = Button(self.frameSort, text = 'Alphabetically')
            alpha.bind('<Button-1>',sortStudsAlpha)
            desc = Button(self.frameSort, text = 'Descending by average grade')
            desc.bind('<Button-1>',sortStudsDesc)
            errorLbl = Label(self.frameSort, text = 'Invalid ID or name! Try again ...')
            lbl.pack(side = LEFT)
            ent.pack(side = LEFT)
            alpha.pack(side = LEFT)
            desc.pack(side = LEFT)       
        
    def failGUI(self,event):
        try:   
            self.errorLabel.configure(text = '')
            self.__printList2(self.__gradeController.fail())                 
        except RepositoryException as ex:
            self.errorLabel.configure(text = ex) 
            
    def bestGUI(self,event):
        try:   
            self.errorLabel.configure(text = '')
            self.__printList3(self.__gradeController.best())                 
        except RepositoryException as ex:
            self.errorLabel.configure(text = ex)
        
    def topDiscGUI(self,event):
        try:   
            self.errorLabel.configure(text = '')
            self.__printList3(self.__gradeController.topDisc())                 
        except RepositoryException as ex:
            self.errorLabel.configure(text = ex) 
             
    def undoGUI(self,event):
        try:   
            self.errorLabel.configure(text = '')
            undoList = self.__undoController.undo()
            self.__studentController,self.__disciplineController,self.__gradeController = deepcopy(undoList[0]), deepcopy(undoList[1]), deepcopy(undoList[2])           
        except RepositoryException as ex:
            self.errorLabel.configure(text = ex)
        
    def redoGUI(self,event):
        try:   
            self.errorLabel.configure(text = '')
            redoList = self.__undoController.redo()
            self.__studentController,self.__disciplineController,self.__gradeController =  deepcopy(redoList[0]), deepcopy(redoList[1]), deepcopy(redoList[2])                 
        except RepositoryException as ex:
            self.errorLabel.configure(text = ex) 