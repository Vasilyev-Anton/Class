class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_avg_hw_grade(self):
        coast = 0
        sum_hw = 0
        for v in self.grades.values():
            for i in v:
                coast += 1
                sum_hw += i
        avg_hw = sum_hw / coast
        return round(avg_hw, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return self.get_avg_hw_grade() < other.get_avg_hw_grade()

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.get_avg_hw_grade()} \nКурсы в процессе обучения: {",".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def get_avg_lc_grade(self):
        coast = 0
        sum_lc = 0
        for v in self.grades.values():
            for i in v:
                coast += 1
                sum_lc += i
        avg_lc = sum_lc / coast
        return round(avg_lc, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.get_avg_lc_grade() < other.get_avg_lc_grade()

    def __str__(self):
        res = (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.get_avg_lc_grade()}')
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress or course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name} \nФамилия: {self.surname}')
        return res


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['GIT']

student = Student('Poul', 'McCartney', 'Male')
student.courses_in_progress += ['Python']
student.finished_courses += ['GIT']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'GIT']

reviewer = Reviewer('Tom', 'Hanks')
reviewer.courses_attached += ['Python', 'GIT']

lecturer = Lecturer('Albert', 'Einstein')
lecturer.courses_attached += ['Python']
lecturer.courses_attached += ['GIT']

student.rate_lc(lecturer, 'Python', 10)
student.rate_lc(lecturer, 'Python', 10)
student.rate_lc(lecturer, 'GIT', 9)

cool_lecturer = Lecturer('Donald', 'Trump')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']

best_student.rate_lc(cool_lecturer, 'Python', 9)
best_student.rate_lc(cool_lecturer, 'Python', 9)
best_student.rate_lc(cool_lecturer, 'GIT', 10)


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'GIT', 9)

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'GIT', 9)

print(best_student)
print(student)

print(cool_reviewer)
print(reviewer)

print(lecturer)
print(cool_lecturer)

print(best_student < student)
print(lecturer < cool_lecturer)


students_list = [
    {'Python': ['Adam Smith', 'Karl Marx', 'John Keynes']},
    {'GIT': ['John Keynes', 'Karl Marx']}
]
lecturers_list = ['Albert Einstein', 'Stephen Hawking', 'Thomas Edison']

def average_grade_of_students_courses(students_list):
    grades_course = {}
    avg_grade_of_students_courses = 0
    for course in students_list:
        for course_name, student in course.items():
            for name in student:
                i = input(f"Введите оценку за курс {course_name} {name}'s: ")
                if course_name in grades_course.keys():
                    grades_course[course_name].append(i)
                else:
                    grades_course[course_name] = [i]

    for k, v in grades_course.items():
        for i, el in enumerate(v):
            v[i] = int(el)

    for course, grades in grades_course.items():
        avg_grade_of_students_courses = {k: sum((v)) / len(v) for k, v in grades_course.items()}

    for k, v in avg_grade_of_students_courses.items():
            print(f"Средняя оценка по курсу {k}: {round(v, 1)}")

def average_grade_of_lecturer_courses(lecturers_list):
    grades_course = {}
    for lecturer in lecturers_list:
        course_name = input(f"Введите курс, который читает {lecturer}: ")
        grade = input(f"Введите оценку за лекции по {course_name} лектора {lecturer}: ")
        if course_name in grades_course.keys():
            grades_course[course_name].append(grade)
        else:
            grades_course[course_name] = [grade]

    for k, v in grades_course.items():
            for i, el in enumerate(v):
                v[i] = int(el)

    for course, grades in grades_course.items():
        avg_grade_of_lecturer_courses = {k: sum((v)) / len(v) for k, v in grades_course.items()}

    for k, v in avg_grade_of_lecturer_courses.items():
            print(f"Средняя оценка по курсу {k}: {round(v, 1)}")

average_grade_of_lecturer_courses(lecturers_list)
average_grade_of_students_courses(students_list)