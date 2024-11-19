class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def give_lecture(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            student.set_grade(course, grade)
        else:
            print(f"Лектор {self.name} {self.surname} не может выставить оценку за курс '{course}'.")

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_course(self, course):
        self.finished_courses.append(course)

    def add_course_in_progress(self, course):
        self.courses_in_progress.append(course)

    def set_grade(self, course, grade):
        if course in self.courses_in_progress:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]
        else:
            print(f"Студент {self.name} {self.surname} не изучает курс '{course}'.")