# todo: implement tests for problemrepo
from ro.ubb.studentsapp.domain.problementity import Problem
from ro.ubb.studentsapp.repository.problemrepository import Problem_repository

# def setup():
#     discipline_repo = Discipline_repository()
#     discipline_repo.save(Discipline(1, 'analiza', 20))
#     discipline_repo.save(Discipline(2, 'logica', 44))
#     discipline_repo.save(Discipline(3, 'math', 21))
#     return discipline_repo
#
# def test_save():
#     discipline_repo = setup()
#     assert (len(discipline_repo.find_all()) == 3)
#
#     assert (discipline_repo.find_by_id(2).id == 2)
#     assert (discipline_repo.find_by_id(2).name == 'logica')
#     assert (discipline_repo.find_by_id(3).credits == 21)
#
#     try:
#         discipline_repo.save(Discipline(1, 'algebra', 18))
#         assert False
#     except ValueError:
#         assert True
#
# def test_find_all():
#     discipline_repo = setup()
#     assert (len(discipline_repo.find_all()) == 3)
#     assert (isinstance(discipline_repo.find_all(),list))
def setup():
    problem_repo = Problem_repository()
    problem_repo.save(Problem(3, 1, 'palindrom', '12.11.2024'))
    problem_repo.save(Problem(1,1,'palindrom','12.11.2024'))
    problem_repo.save(Problem(2,2,'divizor','11.11.2024'))

    return problem_repo

def test_save():
    problem_repo = setup()
    assert (len(problem_repo.find_all())==3)
    assert (problem_repo.find_by_lab(2) is not None)
    ###urm 4 asserturi inseamna ca find_by_lab de lab ul(cheia) unei pb returneaza ceva, deci pb e salvata
    assert (problem_repo.find_by_lab(2).lab == 2)
    assert (problem_repo.find_by_lab(2).nr == 2)
    assert (problem_repo.find_by_lab(2).descriere == 'divizor')
    assert (problem_repo.find_by_lab(2).deadline == '11.11.2024')
    try:
       problem_repo.save(Problem(1,1,'palindrom','12.11.2024'))
       assert False
    except ValueError:
        assert True

def test_find_all():
    problem_repo = setup()
    assert (len(problem_repo.find_all())==3)
    assert (isinstance(problem_repo.find_all(),list ))

def test_all_problems_with_same_number():
    problem_repo = setup()
    assert (len(problem_repo.all_problems_with_same_number(Problem(1,1,'palindrom', '12.11.2024')))==2)

def sorted_all_problems():
    problem_repo = setup()
    assert (len(problem_repo.sorted_all_problems()) == 3)
    # assert (list(problem_repo.sorted_all_problems().keys())==[1,2,3])



def test_all_problemrepo():
    test_save()
    test_find_all()
    test_all_problems_with_same_number()
    sorted_all_problems()


if __name__ == '__main__':
    test_all_problemrepo()



