#todo: implement service for discipline
from ro.ubb.studentsapp.domain.problementity import Problem

class ProblemService:
    def __init__(self,problem_repository):
        self.__problem_repository = problem_repository

    def find_by_lab(self,lab):
        return self.__problem_repository.find_by_lab(lab)

    def add_problem(self, lab, nr, descriere, deadline):
        problem = Problem(lab, nr, descriere, deadline)
        self.__problem_repository.save(problem)

    def get_all_problems(self):
        return self.__problem_repository.find_all()

    def get_all_problems_w_same_nr(self,lab):
        if self.__problem_repository.find_by_lab(lab) is None:
            raise ValueError(f"No problem with lab {lab}")
        problem = self.__problem_repository.find_by_lab(lab)
        # self.__problem_repository.all_problems_with_same_number(problem)
        return self.__problem_repository.all_problems_with_same_number(problem)

    def get_all_problems_sorted(self):
        return self.__problem_repository.sorted_all_problems()









