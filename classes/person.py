import datetime


class Person(object):
    def __init__(self, full_name: str, age: int, gender: str):
        self.full_name = full_name
        self.gender = gender
        self.age = age

    def print_person_info(self):
        print(f'Person: {self.full_name}, ({self.gender}), {self.age} years old')

    def get_birth_years(self):
        return datetime.date.today().year - int(self.age)


