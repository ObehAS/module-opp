class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course].append(grade)
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            print(f"Студент {self.name} {self.surname} не может оценить лектора {lecturer.name} {lecturer.surname} по курсу '{course}'.")

    def get_average_grade(self):
        if not self.grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count if total_count > 0 else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.get_average_grade():.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def get_average_grade(self):
        if not self.lecturer_grades:
            return 0
        total_grades = sum(sum(grades) for grades in self.lecturer_grades.values())
        total_count = sum(len(grades) for grades in self.lecturer_grades.values())
        return total_grades / total_count if total_count > 0 else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.get_average_grade():.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print(f"Эксперт {self.name} {self.surname} не может выставить оценку студенту {student.name} {student.surname} за курс '{course}'.")

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"У лекторов:")
