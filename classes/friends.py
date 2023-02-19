from person import Person

my_friends = [
    Person('nelly', 19, 'F'),
    Person('lol', 22, 'M'),
]


def get_older_person(friends):
    older = friends[0]

    for person in friends[1:]:
        if person.age > older.age:
            older = person

    older.print_person_info()


def filter_male_person(friends):
    only_male = list(filter(lambda pers: pers.gender == 'M', friends))

    for person in only_male:
        person.print_person_info()


for friend in my_friends:
    friend.print_person_info()

get_older_person(my_friends)

filter_male_person(my_friends)
