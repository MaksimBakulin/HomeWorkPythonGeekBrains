from os.path import exists
from add_file_csv import creating
from write import writing_scv, writing_txt, get_info
from export import from_file


def view():
    print(from_file('Phonebook.txt'))


def record_info():
    info = get_info()
    writing_scv(info)
    writing_txt(info)


def choice():
    flag = input(
        'Для продолжения работы нажмите "+", или любой символ для завершения работы... ')
    while (flag.lower() == '+'):
        path = 'Phonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            'Введите "+", если хотите добавить данные, и любой другой символ, если хотите просмотреть справочник: ')
        if choice_action.lower() == '+':
            record_info()
        else:
            view()
        flag = input(
            'Для продолжения работы введите "+", или любой символ для завершения работы ')
    print('Программа завершена.')