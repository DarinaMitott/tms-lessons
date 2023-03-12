import sqlite3

db = sqlite3.connect('phonebook.sqlite')
db.execute(f'''create table if not exists book
(
    id           integer
        constraint book_pk
            primary key autoincrement,
    name         TEXT not null
        constraint book_pk2
            unique,
    phone_number TEXT not null
);
''')
db.commit()


def ask_operation():
    return input('''U need to choose an option:
      0. Exit the program
      1. Add a new contact
      2. Display the entire list of conflicts in alphabetical order.
      3. Update contact number
: ''')


def add_contact():
    name, phone_number = input('name: '), input('phone number: ')
    db.execute('insert into book(name, phone_number) values(?, ?);', (name, phone_number))
    db.commit()
    print('ok')


def select_all():
    it = db.execute('SELECT name, phone_number FROM book ORDER BY name;')
    for name, phone in it.fetchall():
        print(f'{name=}: {phone=}')


def update_number():
    name = input('put the name: ')
    new_number = input('put new number: ')
    cur = db.execute('update book set phone_number = ? where name = ?', (new_number, name))
    if not cur.rowcount:
        print(f'User with name {name} does not exist')
    db.commit()


while True:
    operation = ask_operation()
    match operation:
        case '0':
            exit(0)
        case '1':
            add_contact()
        case '2':
            select_all()
        case '3':
            update_number()
        case _:
            print('the option does not exist')
