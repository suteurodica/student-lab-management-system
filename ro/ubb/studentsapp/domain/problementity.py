class Problem:
    def __init__(self, lab, nr, descriere, deadline):
        self.__lab = lab
        self.__nr = nr
        self.__descriere = descriere
        self.__deadline = deadline

    #props + enter

    @property
    def lab(self):
        return self.__lab

    @lab.setter
    def lab(self, lab_value):
        self.__lab = lab_value

    @property
    def nr(self):
        return self.__nr

    @nr.setter
    def nr(self, value):
        self.__nr = value

    @property
    def descriere(self):
        return self.__descriere

    @descriere.setter
    def descriere(self, value):
        self.__descriere = value

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, value):
        self.__deadline = value

    def __str__(self):
        return f"Problem LAB: {self.__lab}, Nr: {self.__nr}, Descriere: {self.__descriere}, Deadline: {self.__deadline}"

    def __eq__(self, other):
        return self.__nr == other.__nr



if __name__ == '__main__':
    problem = Problem(1, 1, 'nr palindrom', "10.11.2024")
    print(problem)
    print(problem.lab)
    problem.lab = 2
    print(problem)




    # discipline = Discipline(1, "bb", 23)
    # print(discipline)
    # print(discipline.name) #instead of get_name()
    # print(discipline.credits)
    # discipline.credits = 15 #instead of set_credits(15)
    # print(discipline.credits)