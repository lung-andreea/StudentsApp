'''
Created on Nov 6, 2016

@author: Andreea
'''
from src.UI.console import Console
from src.UI.gui import GUI
from src.controller.entity_controller import EntityController
from src.controller.grade_controller import GradeController
from src.domain.entities import Grade
from src.repository.entity_file_repo import EntityFileRepository, \
    EntityBinaryFileRepository
from src.repository.entity_repository import EntityRepository
from src.repository.grade_file_repo import GradeFileRepository, \
    GradeBinaryFileRepository
from src.repository.grade_repository import GradeRepository


students = [(1,'Ratiu Cosmina'),(2,'Kiraly Alex'),(3,'Popa Andra'),(4,'Ocian Eduard'),(5,'Groza Segiu'),(6,'Orha Lorena'),(7,'Orha Anca'),(8,'Ghetie Bianca'),(9,'Barnutiu Denis'),(10,'Orosz Denise'),(11,'Stan Cristian'),(12,'Varga Diana'),(13,'Savianu Silvia'),(14,'Mada Felix'),(15,'Daraban Bianca')]
disciplines = [(1,'Mate'),(2,'Romana'),(3,'Engleza'),(4,'Info'),(5,'Sport')]
enrolled = [(1,1),(1,2),(1,5),(2,2),(2,3),(2,4),(3,4),(3,2),(3,1),(4,3),(4,2),(4,4),(5,1),(5,3),(5,5),(6,2),(6,4),(6,5),(7,2),(7,3),(7,5),(8,1),(8,2),(8,4),(9,2),(9,3),(9,4),(10,1),(10,4),(10,5),(11,2),(11,4),(11,5),(12,1),(12,3),(12,4),(13,2),(13,3),(13,5),(14,1),(14,2),(14,5),(15,3),(15,4),(15,5)]
grades = [Grade(1,1,10),Grade(1,2,8.4),Grade(1,5,5.2),Grade(2,2,6.5),Grade(2,3,7),Grade(2,4,10),Grade(3,4,7),Grade(3,2,8.7),Grade(3,1,3.4),Grade(4,3,3.5),Grade(4,2,6.7),Grade(4,4,4.5),Grade(5,1,7.8),Grade(5,3,8.7),Grade(5,5,9.8),Grade(6,2,9),Grade(6,4,7.6),Grade(6,5,8.8),Grade(7,2,6.7),Grade(7,3,8.9),Grade(7,5,7.6),Grade(8,1,4.5),Grade(8,2,4.5),Grade(8,4,5.6),Grade(9,2,4.8),Grade(9,3,8.9),Grade(9,4,7.5),Grade(10,1,7.5),Grade(10,4,8.9),Grade(10,5,9.3),Grade(11,2,10),Grade(11,4,8.5),Grade(11,5,8.5),Grade(12,1,7.5),Grade(12,3,4),Grade(12,4,8),Grade(13,2,8.2),Grade(13,3,9.4),Grade(13,5,8.5),Grade(14,1,8.4),Grade(14,2,7.5),Grade(14,5,8.2),Grade(15,3,8.6),Grade(15,4,8.5),Grade(15,5,2)]



'''Scrie fisierele de la inceput'''
# miau1 = EntityFileRepository('student_file')
# miau1.writeToFile(students)
# miau2 = EntityFileRepository('discipline_file')
# miau2.writeToFile(disciplines)
# miau3 = GradeFileRepository("enrolled_file","grade_file")
# miau3.writeToFile(enrolled, grades)
   
# miau1 = EntityBinaryFileRepository('students_binary')
# miau1.writeToFile(students)
# miau2 = EntityBinaryFileRepository('discipline_binary')
# miau2.writeToFile(disciplines)
# miau3 = GradeBinaryFileRepository("enrolled_binary","grade_binary")
# miau3.writeToFile(enrolled, grades)



''' in-memory '''
studentRepo = EntityRepository(students)
disciplineRepo = EntityRepository(disciplines)
gradeRepo = GradeRepository(studentRepo,disciplineRepo,enrolled,grades)

''' text file '''
# studentRepo = EntityFileRepository("student_file")
# studentRepo.setEntities(studentRepo.readFromFile())
# disciplineRepo = EntityFileRepository("discipline_file")
# disciplineRepo.setEntities(disciplineRepo.readFromFile())
# gradeRepo = GradeFileRepository("enrolled_file","grade_file")
# gradeRepo.students = EntityRepository(studentRepo.readFromFile())
# gradeRepo.disciplines = EntityRepository(disciplineRepo.readFromFile())
# gradeRepo.enrolled[:] = gradeRepo.readEnrolled()
# # print(gradeRepo.readEnrolled())
# gradeRepo.grades = gradeRepo.readGrades()

''' binary file '''
# studentRepo = EntityBinaryFileRepository('students_binary')
# disciplineRepo = EntityBinaryFileRepository('discipline_binary')
# gradeRepo = GradeBinaryFileRepository('enrolled_binary','grade_binary')
# studentRepo.setEntities(studentRepo.readBinaryFile())
# disciplineRepo.setEntities(disciplineRepo.readBinaryFile())
# gradeRepo.students = EntityRepository(studentRepo.readBinaryFile())
# gradeRepo.disciplines = EntityRepository(disciplineRepo.readBinaryFile())
# gradeRepo.enrolled[:] = gradeRepo.readEnrolledFromBinary()
# gradeRepo.grades = gradeRepo.readGradesFromBinary()


studentController = EntityController(studentRepo)
disciplineController = EntityController(disciplineRepo)
gradeController = GradeController(gradeRepo)


console = Console(studentController,disciplineController,gradeController)
gui = GUI(studentController,disciplineController,gradeController)


# SWITCH BETWEEN CONSOLE AND GUI

# console.runApp()
gui.startGUI()

# studentRepo.writeToFile(studentController.repository.getAll())
# disciplineRepo.writeToFile(disciplineController.repository.getAll())
# gradeRepo.writeToFile(gradeController.repository.enrolled, gradeController.repository.grades)