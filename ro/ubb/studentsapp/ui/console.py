import traceback


class StudentConsole:
    def __init__(self, student_service, problem_service):
        self.__student_service = student_service
        self.__problem_service = problem_service




    def __add_student(self):
        try:
            id = int(input("Enter student id: "))
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            try:
                self.__student_service.add_student(id, name, grade)
            except ValueError:
                print(f"Duplicate entry for {id}")
                traceback.print_exc()

        except ValueError as err:
            print("Id /grade must be integers", err)
            traceback.print_exc()



    def __add_problem(self):
        try:
            lab = int(input("Enter problem lab: "))
            nr = int(input("Enter problem nr: "))
            descriere = input("Enter problem descriere: ")
            deadline = input("Enter problem deadline: ")
            try:
                self.__problem_service.add_problem(lab, nr, descriere, deadline)

            except ValueError:
                print(f"Duplicate entry for {lab}")
        except ValueError as err:
            print("lab /nr must be integers", err)
            traceback.print_exc()

    def __afisare_probleme_cu_acelasi_nr_ca_pb_cu_laboratorul_dat(self):
        try:
            lab = int(input("Enter problem lab: "))
            try:
                print(*self.__problem_service.get_all_problems_w_same_nr(lab))
            except ValueError:

                print(f"Problema cu laboratorul {lab} nu exista")

        except ValueError as err:
            print("lab must be integer", err)




    def __afisare_studenti(self):
        print(*self.__student_service.get_all_students())

    def __afisare_studenti_cu_nota_mai_mare_decat_5(self):
        print(*self.__student_service.get_all_students_with_grater_grade_than_5())

    def __afisare_probleme(self):
        print(*self.__problem_service.get_all_problems())

    def __afisare_probleme_sortate_dupa_lab(self):
        print(*self.__problem_service.get_all_problems_sorted(), sep="\n")

    def __afisare_student_max(self):
        print(self.__student_service.student_with_max_grade())

    def __afisare_primii_20_la_suta_din_studenti(self):
        print(*self.__student_service.get_top_20_percent_students(), sep="\n")

    def __print_options(self):
        print("1:Pentru afisare\n"
              "2:Pentru adaugare\n"
              "3:Pentru adaugare problema\n"
              "4:Pentru afisare probleme\n"
              "5:Pentru afisare studentilor cu nota mai mare sau egala cu 5\n"
              "6:Pentru afisarea unui student cu nota maxima\n"
              "7:Pentru afisarea problemelor cu acelasi numar ca si cea cu laboratorul dat\n"
              "8:Pentru afisarea problemelor in ordine crescatoare dupa laborator\n"
              "9:Pentru afisarea primilor 20 % studenti"

              "X:Pentru iesire\n")

    def run_menu(self):
        dict_optiuni = {1: self.__afisare_studenti, 2: self.__add_student, 3: self.__add_problem,
                        4: self.__afisare_probleme, 5: self.__afisare_studenti_cu_nota_mai_mare_decat_5,
                        6: self.__afisare_student_max, 7: self.__afisare_probleme_cu_acelasi_nr_ca_pb_cu_laboratorul_dat,
                        8: self.__afisare_probleme_sortate_dupa_lab, 9: self.__afisare_primii_20_la_suta_din_studenti}

        while True:
            self.__print_options()
            optiune = input("Optiune= ")
            if optiune == "x":
                break
            try:
                optiune = int(optiune)
                print("option OK") #daca continua inseamna ca optiunea e ok, nu a intrat in blocul except
                dict_optiuni[optiune]()
            except ValueError:
                print("exception in reading options")
            except KeyError:
                print("option not implemented")
            print("after try except")

# def ui_add_student(all_students):
#     try:
#         id = int(input("Enter student id: "))
#         name = input("Enter student name: ")
#         grade = int(input("Enter student grade: "))
#         try:
#             add_student(all_students, id, name, grade)
#         except ValueError:
#             print(f"Duplicate entry for {id}")
#
#     except ValueError as err:
#         print("Id /grade must be integers")
#         traceback.print_exc()
#
#
#

#
# def print_options():
#     print("1:Pentru afisare\n"
#           "2:Pentru adaugare\n"
#           "X:Pentru iesire\n")
#
#
# def afisare_studenti(all_students):
#     print(all_students)
#
#
# def run_menu():
#     all_students = []
#     dict_optiuni = {1: afisare_studenti, 2: ui_add_student}
#     while True:
#         print_options()
#         optiune = input("Optiune= ")
#         if optiune == "x":
#             break
#         try:
#             optiune = int(optiune)
#             print("option OK")
#             dict_optiuni[optiune](all_students)
#         except ValueError:
#             print("exception in reading options")
#         except KeyError:
#             print("option not implemented")
#         print("after try except")
