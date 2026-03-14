class Student:
    # nr=0
    def __init__(self, id, name, grade):
        self.__id = id
        self.__name = name
        self.__grade = grade

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_grade(self, grade):
        self.__grade = grade

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def __str__(self):
        # return str(self.__id) + ' ' + self.__name + ' ' + str(self.__grade)
        return f"STUDENTT ID: {self.__id}, Name: {self.__name}, Grade: {self.__grade}"

    # def __eq__(self, other):
    #     if isinstance(other, Student):
    #         return self.get_id() == other.get_id() and self.get_name() == other.get_name() and self.get_grade() == other.get_grade()
    #     return False


# def create_student(id, name, grade):
#     # student_dict = dict()
#     # student_dict['id'] = id
#     # student_dict['name'] = name
#     # student_dict['grade'] = grade
#     # return student_dict
#
#     # student = {"id": id, "name": name, "grade": grade}
#     # return student
#
#     return {"id": id, "name": name, "grade": grade}
#
#
# def get_id(student):
#     return student["id"]
#
#
# def set_id(student, id):
#     student["id"] = id
#
#
# def get_name(student):
#     return student["name"]
#
#
# def set_name(student, name):
#     student["name"] = name
#
#
# def get_grade(student):
#     return student["grade"]
#
#
# def set_grade(student, grade):
#     student["grade"] = grade
#


if __name__ == '__main__':
    s = Student(1, 'aaaa', 10)
    print(s.get_name())
    s.set_name('bbbbb')
    print(s.get_name())
    print(s)
