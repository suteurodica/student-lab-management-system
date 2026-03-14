# todo: implement tests for discipline service
# from ro.ubb.studentsapp.domain.problementity import Discipline
# from ro.ubb.studentsapp.repository.problemrepository import Discipline_repository
# from ro.ubb.studentsapp.service.disciplineservice import DisciplineService
#
# def test_disciplineservice():
#
#     discipline_repository = Discipline_repository()
#     discipline_operations = DisciplineService(discipline_repository)
#     discipline_operations.add_discipline(1, 'analiza', 20)
#     discipline_operations.add_discipline(2,'logica', 44)
#     assert len(discipline_operations.get_all_disciplines()) == 2
#
#     try:
#         discipline_operations.add_discipline(1, 'algebra', 20)
#         assert False
#     except ValueError:
#         assert True
from ro.ubb.studentsapp.repository.problemrepository import Problem_repository
from ro.ubb.studentsapp.service.problemservice import ProblemService

def setup():
    problem_repo = Problem_repository()
    problem_service = ProblemService(problem_repo)
    problem_service.add_problem(1, 1, 'palindrom', '11.11')
    problem_service.add_problem(2, 1, 'divi', '12.12')
    problem_service.add_problem(3, 1, 'divi', '12.12')
    return problem_service

def test_add_problem():
    problem_repo=Problem_repository()
    problem_service = ProblemService(problem_repo)
    problem_service.add_problem(1, 1, 'palindrom', '11.11')
    problem_service.add_problem(2, 1, 'divi', '12.12')
    assert (len(problem_service.get_all_problems()) == 2)
    try:
        problem_service.add_problem(2,1,'ana', '12.12')
        assert False
    except ValueError:
        assert True

def test_get_all_problems_w_same_nr():

    problem_service = setup()
    assert (len(problem_service.get_all_problems_w_same_nr(1)) == 3)
    assert (isinstance(problem_service.get_all_problems_w_same_nr(1), list))
    assert ((problem_service.get_all_problems_w_same_nr(1)[0]) == problem_service.get_all_problems_w_same_nr(1)[2])


def test_all_problemsoperatiosns():
    test_add_problem()
    test_get_all_problems_w_same_nr()









if __name__ == '__main__':
    test_all_problemsoperatiosns()


