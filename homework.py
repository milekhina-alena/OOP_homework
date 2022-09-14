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
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
         and course in self.courses_in_progress or course in self.finished_courses):
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
        result = sum(grades_sum) / len(grades_sum)
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a student")
            return
        return self._Student__avg_score() < other._Student__avg_score()


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


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __avg_score(self):
        grades_sum = []
        for grades in self.grades.values():
            grades_sum += grades
        result = sum(grades_sum) / len(grades_sum)
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a lecturer")
            return
        return self._Lecturer__avg_score() < other._Lecturer__avg_score()

    def __str__(self):
        return(f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self._Lecturer__avg_score()}''')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and 
        course in student.courses_in_progress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return(f'''Имя: {self.name}
Фамилия: {self.surname}''')



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

worst_student = Student('Brad', 'Pitt', 'your_gender')
worst_student.courses_in_progress += ['Введение в программирование']
worst_student.courses_in_progress += ['Git']
worst_student.finished_courses += ['Python']


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']
cool_mentor.courses_attached += ['Введение в программирование']

some_mentor = Mentor('Any', 'Buddy')
some_mentor.courses_attached += ['Python']
some_mentor.courses_attached += ['Git']
some_mentor.courses_attached += ['Введение в программирование']


bad_reviewer = Reviewer('Roy', 'Black')
bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['Git']
bad_reviewer.courses_attached += ['Введение в программирование']
bad_reviewer.rate_hw(best_student, 'Python', 8)
bad_reviewer.rate_hw(best_student, 'Git', 5)
bad_reviewer.rate_hw(best_student, 'Введение в программирование', 7)
bad_reviewer.rate_hw(worst_student, 'Python', 1)
bad_reviewer.rate_hw(worst_student, 'Git', 2)
bad_reviewer.rate_hw(worst_student, 'Введение в программирование', 3)


some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
some_reviewer.courses_attached += ['Введение в программирование']
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Git', 10)
some_reviewer.rate_hw(best_student, 'Введение в программирование', 10)
some_reviewer.rate_hw(worst_student, 'Python', 6)
some_reviewer.rate_hw(worst_student, 'Git', 8)
some_reviewer.rate_hw(worst_student, 'Введение в программирование', 4)


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached.append('Python')
some_lecturer.courses_attached.append('Git')
some_lecturer.courses_attached.append('Введение в программирование')


awesome_lecturer = Lecturer('Albus', 'Dumbledore')
awesome_lecturer.courses_attached.append('Python')
awesome_lecturer.courses_attached.append('Git')
awesome_lecturer.courses_attached.append('Введение в программирование')


best_student.rate_lecture(some_lecturer, 'Python', 8)
best_student.rate_lecture(some_lecturer, 'Git', 5)
best_student.rate_lecture(some_lecturer, 'Введение в программирование', 7)
best_student.rate_lecture(awesome_lecturer, 'Python', 10)
best_student.rate_lecture(awesome_lecturer, 'Git', 10)
best_student.rate_lecture(awesome_lecturer, 'Введение в программирование', 10)

worst_student.rate_lecture(some_lecturer, 'Python', 7)
worst_student.rate_lecture(some_lecturer, 'Git', 9)
worst_student.rate_lecture(some_lecturer, 'Введение в программирование', 6)
worst_student.rate_lecture(awesome_lecturer, 'Python', 8)
worst_student.rate_lecture(awesome_lecturer, 'Git', 10)
worst_student.rate_lecture(awesome_lecturer, 'Введение в программирование', 9)

print(best_student.grades)
print(some_lecturer._Lecturer__avg_score())
print(some_lecturer.grades)
print(best_student)
print(worst_student)
print(best_student < worst_student)
print(awesome_lecturer)
print(some_lecturer)
print(some_lecturer > awesome_lecturer)
print(some_reviewer)
print(bad_reviewer)
print(best_student._Student__avg_score())
print(worst_student._Student__avg_score())


student_list = [best_student, worst_student]

def avg_student_score(student, course):
    grade_list = []
    for student in student_list:
        if course in student.grades:
            grade_list += student.grades[course]
        else:
            return 'Error'
        result = sum(grade_list) / len(grade_list)
    return result

print(avg_student_score(student_list, 'Python'))
print(avg_student_score(student_list, 'Git'))
print(avg_student_score(student_list, 'Введение в программирование'))

# print(best_student.grades)
# print(worst_student.grades)

lecturer_list = [some_lecturer, awesome_lecturer]

def avg_lecturer_score(lecturer, course):
    grade_list = []
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            grade_list += lecturer.grades[course]
        else:
            return 'Error'
        result = sum(grade_list) / len(grade_list)
    return result
  
print(avg_lecturer_score(lecturer_list, 'Python'))
print(avg_lecturer_score(lecturer_list, 'Git'))
print(avg_lecturer_score(lecturer_list, 'Введение в программирование'))

# print(some_lecturer.grades)
# print(awesome_lecturer.grades)