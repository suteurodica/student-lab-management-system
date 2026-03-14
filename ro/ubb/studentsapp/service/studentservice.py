# def find_by_id(all_students, id):
#     for student in all_students:
#         if student.get_id() == id:
#             return student
#     return None
#
#
# def add_student(all_students, id, name, grade):
#     if find_by_id(all_students, id) is not None:
#         raise ValueError
#
#     student = Student(id, name, grade)
#     all_students.append(student)
from ro.ubb.studentsapp.domain.studententity import Student


# class StudentOperations:
#     @staticmethod
#     def find_by_id(all_students, id):
#         for student in all_students:
#             if student.get_id() == id:
#                 return student
#         return None
#
#     @staticmethod
#     def add_student(all_students, id, name, grade):
#         if StudentOperations.find_by_id(all_students, id) is not None:
#             raise ValueError
#
#         student = Student(id, name, grade)
#         all_students.append(student)

class StudentService:
    def __init__(self, student_repository):
        #self.__all_students=[]
        self.__student_repository = student_repository

    def find_by_id(self, id):
        return self.__student_repository.find_by_id(id)

    def add_student(self, id, name, grade):
        student = Student(id, name, grade)
        self.__student_repository.save(student)

    def get_all_students(self):
        return self.__student_repository.find_all()

    def get_all_students_with_grater_grade_than_5(self):
        return self.__student_repository.students_with_greater_grade_than_5()

    def student_with_max_grade(self):
        return self.__student_repository.student_with_maximal_grade()

    def get_top_20_percent_students(self):
        return self.__student_repository.top_20_percent_students()



