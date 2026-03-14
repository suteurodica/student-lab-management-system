# from ro.ubb.studentsapp.domain.studententity import Student


class StudentRepository:
    def __init__(self):
        # self.__all_students = []
        self.__all_students = dict()
        self.__students_with_greater_grade_than_5 = dict()
        # self.__maxx= 0
        # self.__beststudent = None

    def save(self, student):
        """
        Add a new student to the repository.
        :param student: Student
        :raises: ValueError: if `student.id` does not exist.
        """
        # if self.__find_by_id(student.get_id()) is not None:
        #     raise ValueError(f"Id {id} exists", student.get_id())
        # self.__all_students.append(student)

        if self.find_by_id(student.get_id()) is not None:
            raise ValueError(f"Id {id} exists", student.get_id())
        # self.__all_students.update({student.get_id() : student})
        self.__all_students[student.get_id()] = student

    def find_all(self):
        """
        :return: Returns the list of all students.
        :rtype: list[Student]
        """
        # return self.__all_students
        return list(self.__all_students.values())

    def students_with_greater_grade_than_5(self):
        if self.__all_students is None:
            raise ValueError("No students found")

        for student in self.__all_students.values():
            if student.get_grade() >= 5:
                self.__students_with_greater_grade_than_5[student.get_id()] = student
        return list(self.__students_with_greater_grade_than_5.values())

    def student_with_maximal_grade(self):
        maxx = 0
        for student in self.__all_students.values():
            if student.get_grade() > maxx:
                maxx = student.get_grade()
                beststudent = student
        return beststudent

    def top_20_percent_students(self):
        all_students = list(self.__all_students.values())
        sorted_students = sorted(all_students, key=lambda student: student.get_grade(), reverse=True)
        top_20 = max(1, int(len(sorted_students)* 0.2))
        return sorted_students[:top_20]



    def update(self, student):
        """
        Update the student with the given `student.id`.
        :param student:
        :return:
        :raises: ValueError: if `student.id` does not exist
        """
        if self.find_by_id(student.get_id()) is None:
            raise ValueError("Student ID does not exist")
        self.__all_students[student.get_id()] = student



    def delete_by_id(self, id):
        """
        Delete the student with the given `id`.
        :param id: int
        :return:
        :raises: ValueError if a student with the given `id` does not exist.
        """
        if self.find_by_id(id) is None:
            raise ValueError("Student ID does not exist")
        del self.__all_students[id]


    def find_by_id(self, id):
        """
        Return the student with id {id} if exists else None
        :param id: int
        :return: Student with id {id}
        :rtype: Student | None
        """

        # for student in self.__all_students:
        #     if student.get_id() == id:
        #         return student
        # return None

        # V2
        # try:
        #     return self.__all_students[id]
        # except KeyError:
        #     return None

        # V3
        if id in self.__all_students.keys(): # <=> self.__all_students
            return self.__all_students[id]
        return None

