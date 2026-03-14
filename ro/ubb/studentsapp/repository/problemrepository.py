# todo: implement repo
from ro.ubb.studentsapp.domain.problementity import Problem

class Problem_repository:

 def __init__(self):
     self.__all_problems = dict()
     # self.__all_pb_with_same_number = []

 def find_by_lab(self,lab):
     if lab in self.__all_problems.keys():
         return self.__all_problems[lab]
     return None

 def save(self,problem):
     if self.find_by_lab(problem.lab) is not None:
         raise ValueError(f"Problema cu laboratorul {problem.lab} exista")
     self.__all_problems[problem.lab] = problem

 def update(self,problem):
     if self.find_by_lab(problem.lab) is None:
         raise ValueError(f"Problema cu laboratorul {problem.lab} nu exista")
     self.__all_problems[problem.lab] = problem

 def delete(self,lab):
     if self.find_by_lab(lab) is None:
         raise ValueError(f"Problema cu laboratoul {lab} nu exista")
     del self.__all_problems[lab]

 def find_all(self):
     return list(self.__all_problems.values())

 def all_problems_with_same_number(self,problem):

     all_pb_with_same_number = []
     for pb in self.__all_problems.values():
         if problem == pb:
             all_pb_with_same_number.append(pb)
     return all_pb_with_same_number

 def sorted_all_problems(self):
     return dict(sorted(self.__all_problems.items(), key=lambda x: x[0])).values()

     # dictsorted=()
     # dictsorted=dict(sorted(self.__all_problems.items(), key=lambda x: x[0]))
     # return dictsorted.values()














