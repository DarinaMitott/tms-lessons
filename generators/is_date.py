import re


def is_date(string):
    return re.fullmatch(r'(\d{1,2})-(\d{1,2})-(\d{4})', string) is not None


# ето в процессе я потом зарешаю

# def is_float_number(string):
#     return re.fullmatch(r'\d\.\d', string)
#
#
# if __name__ == '__main__':
#     assert is_float_number('4.5')

