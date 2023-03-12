import random
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


db = sqlite3.connect('bank.sqlite')
db.row_factory = dict_factory
db.execute(f'''create table if not exists bank_accounts
(
    id             integer
        constraint bank_accounts_pk
            primary key autoincrement,
    card_holder    TEXT not null,
    money          REAL not null,
    card_number    TEXT not null,
    account_number TEXT not null
);
''')
db.commit()


def get_random_digits(count: int):
    return ''.join([str(random.randint(0, 9)) for i in range(count)])


class BankAccount(object):
    def __init__(self, card_holder, money=0.0, card_number=None, account_number=None, id=None):
        self._id = id
        self.card_holder = card_holder.upper()
        self.money = money
        self.card_number = get_random_digits(16) if card_number is None else card_number
        self.account_number = get_random_digits(20) if account_number is None else account_number

    def to_dict(self):
        return {
            'card_holder': self.card_holder,
            'money': self.money,
            'card_number': self.card_number,
            'account_number': self.account_number,
        }

    @classmethod
    def get_by_account(cls, account_number):
        cur = db.execute('''select * from bank_accounts where account_number = ?''', [account_number])
        account_dict = cur.fetchone()
        if account_dict is None:
            return
        o = cls(**account_dict)
        return o

    def update_money(self, diff):
        cur = db.execute('''update bank_accounts set money = money + ? where id = ?''', (diff, self._id))
        if not cur.rowcount:
            print(f'failed update money')
        db.commit()

    def transfer(self, account_to, amount):
        cur = db.execute('''update bank_accounts set money = money + ? where id = ?''', (-amount, self._id))
        if not cur.rowcount:
            print(f'failed update money')
            db.rollback()
            return False
        cur = db.execute('''update bank_accounts set money = money + ? where id = ?''', (amount, account_to._id))
        if not cur.rowcount:
            print(f'failed update money')
            db.rollback()
            return False
        db.commit()
        self.refresh_money()
        account_to.refresh_money()
        return True

    def refresh_money(self):
        cur = db.execute('select money from bank_accounts where id = ?', [self._id])
        self.money = cur.fetchone()['money']

    def save(self):
        cur = db.execute('''insert into bank_accounts(card_holder, money, card_number, account_number)
         values(:card_holder, :money, :card_number, :account_number);''', self.to_dict())
        self._id = cur.lastrowid
        db.commit()

    @classmethod
    def list_accounts(cls):
        for item in db.execute('select * from bank_accounts').fetchall():
            yield cls(**item)

    def __repr__(self):
        return f'BankAccount({self.card_holder},{self.money}, {self.card_number}, {self.account_number}, {self._id})'


class Bank(object):
    def open_account(self, card_holder):
        account = BankAccount(card_holder)
        account.save()
        return account

    def add_money(self, account_number, money):
        account = BankAccount.get_by_account(account_number)
        if account is None:
            print('account not found')
            return
        account.update_money(money)

    def transfer_money(self, from_account_number, to_account_number, money):
        account_from = BankAccount.get_by_account(from_account_number)
        if account_from is None:
            print('account_from not found')
            return
        account_to = BankAccount.get_by_account(to_account_number)
        if account_to is None:
            print('account_to not found')
            return
        if not account_from.transfer(account_to, money):
            print('transfer failed')
        else:
            print('transfer is ok')

    def external_money(self,  from_account_number,  money):
        account_from = BankAccount.get_by_account(from_account_number)
        account_from.update_money(-money)


class Controller(object):
    def __init__(self):
        self.bank = Bank()

    def run(self):
        print('Здравствуйте, наш банк открылся!')
        while True:
            print('\nВыберите действие:')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж')
            person_input = int(input('Выберите действие: '))
            match person_input:
                case 0:
                    # save_accounts(self.bank.bank_accounts, self.data_file_name)
                    print('До свидания!')
                    break

                case 1:
                    card_holder = input('put ur name: ')
                    bank_account = self.bank.open_account(card_holder)
                    print(f'Счёт {bank_account.account_number} создан')

                case 2:
                    for account in BankAccount.list_accounts():
                        print(account)

                case 3:
                    account_number = input('put number account for whom u want send money: ')
                    money = float(input('put the sum: '))
                    if money <= 0:
                        print('money must me > 0')
                        continue

                    self.bank.add_money(account_number, money)

                case 4:
                    account = input('ur account number: ')
                    to_account_number = input('for whom account number: ')
                    money_sent = float(input('how many? '))

                    if account == to_account_number:
                        print('they are equal')
                        continue
                    if money_sent <= 0:
                        print('money must me > 0')
                        continue
                    self.bank.transfer_money(account, to_account_number, money_sent)

                case 5:
                    person_account = input('put ur account: ')
                    to_external_account = input('put account number for whom: ')
                    moneyy = float(input('how many: '))
                    if not person_account:
                        print('ur account is invalid')
                        continue
                    if moneyy <= 0:
                        print('money must me > 0')
                        continue

                    self.bank.external_money(person_account, moneyy)
                case _:
                    print('lol')


if __name__ == '__main__':
    controller = Controller()
    controller.run()
