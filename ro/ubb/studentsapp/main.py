
from ro.ubb.studentsapp.domain.studententity import Student
from ro.ubb.studentsapp.domain.problementity import Problem
from ro.ubb.studentsapp.domain.test_studententity import test_all_student_entity
from ro.ubb.studentsapp.domain.test_problementity import  test_all_problem_entity
from ro.ubb.studentsapp.repository.studentrepository import StudentRepository
from ro.ubb.studentsapp.repository.problemrepository import  Problem_repository
from ro.ubb.studentsapp.repository.test_problemrepository import test_all_problemrepo
from ro.ubb.studentsapp.repository.test_studentrepository import test_all_student_repo
from ro.ubb.studentsapp.service.problemservice import  ProblemService
from ro.ubb.studentsapp.service.studentservice import StudentService
from ro.ubb.studentsapp.service.test_problemservice import test_all_problemsoperatiosns
from ro.ubb.studentsapp.service.test_studentservice import test_all_students_operations

from ro.ubb.studentsapp.ui.console import StudentConsole



####################################domain##############################################


##########################################################################################


############################service######################################################

##########################################################################################


#############################################ui#############################################


##########################################################################################

#################################################tests#############################################


#############################################################################################

#############################################main#############################################

def test_all():
    test_all_student_entity()
    test_all_problem_entity()
    test_all_student_repo()
    test_all_problemrepo()
    test_all_students_operations()
    test_all_problemsoperatiosns()




def main():
    print("hello")

    test_all()
    # todo: update tests.

    student_repository = StudentRepository()
    problem_repository = Problem_repository()
    student_service = StudentService(student_repository)
    problem_service = ProblemService(problem_repository)
    student_console = StudentConsole(student_service, problem_service)
    student_console.run_menu()
    # run_menu()

    print("bye")


main()
