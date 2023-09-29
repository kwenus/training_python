
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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        # делаем проверки: что выставляем оценку студенту,
        # что препадаватель закреплен за этим курсом,
        # что студент изучает этот курс
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]   # если курс уже есть, просто добавляем оценку
            else:
                student.grades[course] = [grade]  # если нет, создаем курс в словаре с оценкой
        else:
            return 'Error'    # если сущность не студент, выводим ошибку

student_1 = Student('Kostya', 'Kanatev', 'm')
student_1.finished_courses += ['Git']    # правильно передавать список, а не строку
student_1.courses_in_progress += ['Python']
student_1.grades['Git'] = [10, 10, 10, 10, 10]
student_1.grades['Python'] = [10, 10]

print(student_1.finished_courses)
print(student_1.courses_in_progress)
print(student_1.grades)

mentor_1 = Mentor('Eugene', 'Vafin')
mentor_1.courses_attached += ['Python']
print(mentor_1.courses_attached)

mentor_1.rate_hw(student_1, 'Python', 8)
mentor_1.rate_hw(student_1, 'Python', 7)
mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_1, 'Git', 9) # не работает, тк преподаватель не прикреплен к этому курсу

print(student_1.grades)

mentor_2 = Mentor('Ivan', 'Petrov')

print(mentor_1.rate_hw(mentor_2, 'Python', 10)) # выводит ошибку, тк не является элементом класса Student

