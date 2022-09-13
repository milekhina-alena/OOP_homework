# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}

#     def add_courses(self, course_name):
#         self.finished_courses.append(course_name)


# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []

#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return "Ошибка"

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __avg_score(self):
        grades_sum = []
        for grades in self.grades.values():
            grades_sum += grades
        # print(grades_sum)
        # print(sum(grades_sum))
        # print(len(grades_sum))
        result = sum(grades_sum) / len(grades_sum)
        return result

    # courses_in_progress = ", ".join(self.courses_in_progress)

    def __str__(self):
        return(f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self._Student__avg_score()}
Курсы в процессе изучения: ''' + ', '.join(self.courses_in_progress) + '''
Завершенные курсы: ''' + ', '.join(self.finished_courses))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return "Ошибка"

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses.append('Введение в программирование')

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


#print(best_student.grades)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __avg_score(self):
        grades_sum = []
        for grades in self.grades.values():
            grades_sum += grades
        # print(grades_sum)
        # print(sum(grades_sum))
        # print(len(grades_sum))
        result = sum(grades_sum) / len(grades_sum)
        return result

    def __str__(self):
        return(f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self._Lecturer__avg_score()}''')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return(f'''Имя: {self.name}
Фамилия: {self.surname}''')

# print(Lecturer.mro())
# print(Reviewer.mro())


# bad_reviewer = Reviewer('Roy', 'Black')
# bad_reviewer.courses_attached += ['Python']
# bad_reviewer.rate_hw(best_student, 'Python', 1)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
some_reviewer.courses_attached += ['Введение в программирование']
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Git', 10)
some_reviewer.rate_hw(best_student, 'Введение в программирование', 10)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached.append('Python')
some_lecturer.courses_attached.append('Git')
some_lecturer.courses_attached.append('Введение в программирование')

best_student.rate_lecture(some_lecturer, 'Python', 10)
best_student.rate_lecture(some_lecturer, 'Git', 10)
best_student.rate_lecture(some_lecturer, 'Введение в программирование', 8)

# print(best_student.grades)
# print(some_lecturer.avg_score())
# print(some_lecturer.grades)
print(best_student)
