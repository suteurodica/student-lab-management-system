from ro.ubb.studentsapp.domain.problementity import Problem

def test_create_problem():
    p=Problem(1,1, "nr palindrom", "10.11.2024")
    assert (p.lab == 1)
    assert p.nr == 1
    assert p.descriere == 'nr palindrom'
    assert p.deadline == "10.11.2024"


def test_props_setter():
    p=Problem(1,1, "nr palindrom", "10.11.2024")
    p.lab = 2
    assert (p.lab == 2)
    p.descriere = "pb cu studenti"
    assert p.descriere == "pb cu studenti"

def test_eq():
    p1=Problem(1,1, "nr palindrom", "10.11.2024")
    p2=Problem(2,1, "nr palindrom", "10.11.2024")
    assert p1==p2

def test_all_problem_entity():
    test_create_problem()
    test_props_setter()
    test_eq()

if __name__ == '__main__':
    test_all_problem_entity()

