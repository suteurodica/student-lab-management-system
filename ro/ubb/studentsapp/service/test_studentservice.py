from ro.ubb.studentsapp.domain.studententity import Student
from ro.ubb.studentsapp.repository.studentrepository import StudentRepository
from ro.ubb.studentsapp.service.studentservice import StudentService
#trebuie sa

# def test_add_student():
#     student_list = []
#     add_student(student_list, id = 1, name = 'aaa', grade=9)
#     assert len(student_list) == 1
#     student = student_list[0]
#     assert get_id(student) == 1
#     assert get_name(student) == 'aaa'
#     assert get_grade(student) == 9
#     try:
#         add_student(student_list, id = 1, name = 'bbb', grade=10)
#         assert False
#     except ValueError:
#         assert True
# assert add_student()


def test_add_student():
    # student_list = []
    # add_student(student_list, id=1, name='aaa', grade=9)
    # assert len(student_list) == 1
    # student = student_list[0]
    # assert (student.get_id() == 1)
    # assert (student.get_name() == 'aaa')
    # assert (student.get_grade() == 9)
    # try:
    #     add_student(student_list, id=1, name='bbb', grade=10)
    #     assert False
    # except ValueError:
    #     assert True

    student_repository = StudentRepository()
    student_operations = StudentService(student_repository)
    student_operations.add_student(1, 'aaa', 9)
    assert len(student_operations.get_all_students()) == 1

    try:
        student_operations.add_student(1, 'bbb', 8)
        assert False
    except ValueError:
        assert True

def test_all_students_operations():
    test_add_student()

    # student = student_operations.get_all_students()[0]
    # assert student.get_name() == 'aaa'
    # assert student.get_id() == 1
    # assert student.get_grade() == 9
    # try:
    #     student_operations.add_student(1, 'bbb', 10)
    #     assert False
    # except ValueError:
    #     assert True


if __name__ == '__main__':
    test_add_student()


# def test_all_student_operations():
#     test_add_student()
