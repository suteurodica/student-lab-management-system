from ro.ubb.studentsapp.domain.studententity import Student


def test_create_student():
    s = Student(1, 'aaaaaa', 10)
    assert (s.get_id() == 1)
    assert (s.get_name() == 'aaaaaa')
    assert (s.get_grade() == 10)

def test_get_set():
    s = Student(1, 'aaaaaa', 10)
    s.set_id(2)
    assert (s.get_id() == 2)
    s.set_name('aaabbb')
    assert (s.get_name() == 'aaabbb')
    s.set_grade(9)
    assert (s.get_grade() == 9)

def test_all_student_entity():
    test_create_student()
    test_get_set()

if __name__ == '__main__':
    test_all_student_entity()