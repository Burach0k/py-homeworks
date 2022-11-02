class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        else:
            return NotImplemented

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        sum_grade = 0
        grade_count = 0

        for course, grades in self.grades:
            for grade in grades:
                sum_grade += grade
                grade_count += 1
        
        if grade_count > 0:
            return sum_grade / grade_count
        else:
            return 0
    
    def __str__(self):
        name = f'Имя: {self.name}\n'
        surname = f'Фамилия: {self.surname}\n'
        average_grade = f'Средняя оценка за домашние задания: {self.get_average_grade()}\n'
        courses_in_progress = f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        finished_courses = f'Завершенные курсы: {", ".join(self.finished_courses)}'

        return name + surname + average_grade + courses_in_progress + finished_courses

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}
    
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() == other.get_average_grade()
        else:
            return NotImplemented
    
    def get_average_grade(self):
        sum_grade = 0
        grade_count = 0

        for course, grades in self.grades.items():
            for grade in grades:
                sum_grade += grade
                grade_count += 1
        
        if grade_count > 0:
            return sum_grade / grade_count
        else:
            return 0

    def __str__(self):
        name = f'Имя: {self.name}\n'
        surname = f'Фамилия: {self.surname}\n'
        average_grade = f'Средняя оценка за домашние задания: {self.get_average_grade()}'

        return name + surname + average_grade

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name = f'Имя: {self.name}\n'
        surname = f'Фамилия: {self.surname}'

        return name + surname

def calculate_students_average_grade_by_course(student_list, course):
    average_grade = 0
    grade_count = 0

    for student in student_list:
        if student.grades and student.grades[course]:
            average_grade += sum(student.grades[course]) / len(student.grades[course])
            grade_count += 1
    
    if grade_count > 0:
        return average_grade / grade_count
    else:
        return 0

def calculate_lecture_average_grade_by_course(lecturer_list, course):
    average_grade = 0
    grade_count = 0

    for lecturer in lecturer_list:
        if lecturer.grades and lecturer.grades[course]:
            average_grade += sum(lecturer.grades[course]) / len(lecturer.grades[course])
            grade_count += 1
    
    if grade_count > 0:
        return average_grade / grade_count
    else:
        return 0

best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python']

best_student_2 = Student('Neruoy', 'Neeman', 'ne_your_gender')
best_student_2.courses_in_progress += ['Python']

cool_lecturer_1 = Lecturer('Some_Lecturer', 'Buddy')
cool_lecturer_1.courses_attached += ['Python']

cool_lecturer_2 = Lecturer('Nesome_Lecturer', 'Nebuddy')
cool_lecturer_2.courses_attached += ['Python']

cool_reviewer_1 = Reviewer('Some_Reviewer', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Nesome_Reviewer', 'Nebuddy')
cool_reviewer_2.courses_attached += ['Python']


best_student_1.rate_lecture(cool_lecturer_1, 'Python', 3)
best_student_2.rate_lecture(cool_lecturer_2, 'Python', 4)

print(best_student_1)
print(best_student_1 == best_student_2)

print('----------')

print(cool_lecturer_1)
print(cool_lecturer_2)
print(cool_lecturer_1 == cool_lecturer_2)

print('----------')

print(cool_reviewer_1)
print(cool_reviewer_2)
print(cool_reviewer_1 == cool_reviewer_2)

print('----------')

print(calculate_students_average_grade_by_course([best_student_1, best_student_2], 'Python'))
print(calculate_lecture_average_grade_by_course([cool_lecturer_1, cool_lecturer_2], 'Python'))