from ro.ubb.studentsapp.domain.studententity import Student
from ro.ubb.studentsapp.repository.studentrepository import StudentRepository


def setup():
    student_repo = StudentRepository()
    student_repo.save(Student(1, 'aa', 9))
    student_repo.save(Student(2, 'bbb', 10))
    student_repo.save(Student(3, 'ccc', 8))

    student_repo.save(Student(4, 'ddd', 4))
    return student_repo

def test_save():

    student_repo = setup()
    assert (len(student_repo.find_all()) == 4)
    assert (student_repo.find_by_id(1).get_id() == 1)
    try:
        student_repo.save(Student(2, 'dddd', 8))
        assert (False)
    except ValueError:
        assert (True)

def test_students_with_greater_grade_than_5():

    student_repo = setup()
    assert (len(student_repo.students_with_greater_grade_than_5()) == 3)

def test_top_20():

    student_repo = setup()
    assert(len(student_repo.top_20_percent_students())==1)
    assert(student_repo.top_20_percent_students()[0].get_id() == 2)



def test_student_with_maximal_grade():

    # student_repo = setup()
    # expected_student = Student(2, 'bbb', 10)
    # assert (student_repo.student_with_maximal_grade() == expected_student )

    student_repo = setup()
    assert (student_repo.student_with_maximal_grade().get_id() == 2 )
    assert (student_repo.student_with_maximal_grade().get_name() == 'bbb' )
    assert (student_repo.student_with_maximal_grade().get_grade() == 10)



def test_find_all():
    student_repo = setup()

    assert (len(student_repo.find_all()) == 4)
    assert (isinstance(student_repo.find_all(), list))


def test_all_student_repo():
    test_save()
    test_find_all()
    test_student_with_maximal_grade()
    test_students_with_greater_grade_than_5()
    test_top_20()

if __name__ == '__main__':
    test_all_student_repo()
