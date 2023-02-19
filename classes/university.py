from student import Student

students1 = [
    Student('lol', 9),
    Student('kek', 7),
    Student('pek', 5),
]


def calc_sum_scholarship(students):
    result_sum = 0
    for student in students:
        result_sum += student.get_scholarship()
    return result_sum


def get_excellent_student_count(students):
    return len(list(filter(Student.is_excellent, students)))


print(calc_sum_scholarship(students1))
print(get_excellent_student_count(students1))
