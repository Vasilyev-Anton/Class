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

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.get_avg_hw_grade()} \nКурсы в процессе обучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}')
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
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
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
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'GIT', 9)

cool_reviewer.rate_hw(student, 'Python', 10)
cool_reviewer.rate_hw(student, 'Python', 10)
cool_reviewer.rate_hw(student, 'Python', 10)
cool_reviewer.rate_hw(student, 'GIT', 9)

print(cool_reviewer)

print(best_student < student)