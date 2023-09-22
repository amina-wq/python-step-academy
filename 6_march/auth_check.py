import re
import os

from datetime import datetime


class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)


def validate(e_mail: str, password: str):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

    if not re.match(email_pattern, e_mail):
        raise ValidationError('Введён некорректный E-mail')
    if not re.match(password_pattern, password):
        raise ValidationError(
            'Пароль должен состоять более чем из 8 символов, '
            'содержать латинские буквы верхнего и нижнего регистров, а также цифры'
        )


if __name__ == '__main__':
    e_mail = input('Введите E-mail: ')
    password = input('Введите пароль: ')

    validate(e_mail, password)
    if not os.path.exists('./user_data'):
        os.mkdir('./user_data')

    user_file_path = f'./user_data/{e_mail}.txt'

    with open(user_file_path, 'a') as file:
        file.write(f'{e_mail}:{password}\t')
        file.write(f'Logged in: {datetime.now()}\n')
