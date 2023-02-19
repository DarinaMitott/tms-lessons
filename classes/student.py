
class Student(object):
    def __init__(self, full_name: str, average_mark: float):
        self.full_name = full_name
        self.average_mark = average_mark

    def get_scholarship(self) -> int:
        if self.average_mark < 6:
            return 60
        elif self.average_mark >= 8:
            return 100
        else:
            return 80

    def is_excellent(self) -> bool:
        return self.average_mark >= 9


students = [
    Student('lol', 9),
    Student('kekl', 7),
    Student('pekl', 5),
]
