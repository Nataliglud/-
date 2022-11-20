class Student:
    some_student = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.some_student.append(self)

    def add_courses (self, course_name):
        self.finished_courses.append(course_name)

    def _average_rate(self):
        sum_grade = 0
        sum_element = 0
        average_rate = 0
        for course, grades in self.grades.items():
            for grade in grades:
                sum_element += 1
                sum_grade += grade
            average_rate = float("{:.1f}".format(sum_grade / sum_element))
        return average_rate

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'Такого студента нет')
            return
        return self._average_rate() < other._average_rate()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}  \nСредняя оценка за домашние задания: {self._average_rate()} \n'\
              f'Курсы в процессе изучения: {",".join(self.courses_in_progress)} \n'\
              f'Завершенные курсы: {",".join(self.finished_courses)}\n'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    some_lecturer = []
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        Lecturer.some_lecturer.append(self)

    def _average_rate(self):
        sum_grade = 0
        sum_element = 0
        average_rate = 0
        for course, grades in self.grades.items():
            for grade in grades:
                sum_element += 1
                sum_grade += grade
            average_rate = float("{:.1f}".format(sum_grade / sum_element))
        return average_rate

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Такого лектора нет')
            return
        return self._average_rate() < other._average_rate()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции {self._average_rate()}\n'
        return res

class Reviewer (Mentor):
    some_reviewer =[]
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        Reviewer.some_reviewer.append(self)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.courses_attached += ['Git', 'Python']
lecturer2 = Lecturer('Петр', 'Петров')
lecturer2.courses_attached +=['Python', 'Git']

student1 = Student('Настя', 'Иванова', 'ж')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student1.rate_hw (lecturer2, 'Git', 5)
student1.rate_hw (lecturer1, 'Python', 7)
student2 = Student('Маша', 'Русских', 'ж')
student2.courses_in_progress += ['Git', 'Python']
student2.finished_courses += ['Введение в программирование']
student2.rate_hw (lecturer1, 'Git', 6)
student3 = Student('Саша', 'Чупин', 'м')
student3.courses_in_progress += ['Python', 'Git']
student3.finished_courses += ['Введение в программирование']
student3.rate_hw (lecturer2, 'Python', 10)
student3.rate_hw (lecturer1, 'Python', 4)

reviewer1 = Reviewer('Макс', 'Иванов')
reviewer1.courses_attached += ['Git', 'Python']
reviewer1.rate_hw (student1, 'Git', 5)
reviewer1.rate_hw (student2, 'Python', 8)
reviewer1.rate_hw (student3, 'Python', 10)
reviewer2 = Reviewer('Петр', 'Ван')
reviewer2.courses_attached +=['Python']
reviewer2.rate_hw (student1, 'Python', 5)
reviewer2.rate_hw (student2, 'Python', 6)
reviewer2.rate_hw (student3, 'Python', 4)

print(student1.grades)
print(student2.grades)
print(student3.grades)
print(lecturer1.grades)
print(lecturer2.grades)

print(*Student.some_student)
print(*Reviewer.some_reviewer)
print(*Lecturer.some_lecturer)

print(lecturer1<lecturer2)
print(student1<student2)
print(student2<student3)
print(student1<student3)

def av_grades(course='Python'):
    av_list = []
    for student in Student.some_student:
        if course in student.courses_in_progress or course in student.finished_courses:
            for grades in student.grades.get(course):
                av_list.append(grades)
    average = sum(av_list) / len(av_list)
    return print(average)
av_grades()

def av_grades(course='Python'):
    av_list = []
    for lecturer in Lecturer.some_lecturer:
        if course in lecturer.courses_attached:
            for grades in lecturer.grades.get(course):
                av_list.append(grades)
    average = sum(av_list) / len(av_list)
    return print(average)
av_grades()



