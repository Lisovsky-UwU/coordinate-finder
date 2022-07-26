from coordinate_finder import api_requests
from coordinate_finder.settings import change as change_settings
from msvcrt import getch
import os

# query error text
ErrorText = 'Ошибка выполнения запроса\n' \
            'Убедитесь в следующем:\n' \
            '1. Вы подключены к интернету\n' \
            '2. Вы ввели корректный адрес\n' \
            '3. В настройках указаны верные базовый URL и API ключ'


# function to get the address
# return 1 - when index is not int
# return 2 - when index out of range
# return other error code on error
def get_address():
    address = input('Введите адрес для поиска: ')
    list_addresses = api_requests.get_addresses_on_query(address)
    if type(list_addresses) == int:
        return list_addresses

    print('Список возможных вариантов:')
    for i in range(len(list_addresses)):
        print(f'{i + 1}.' + list_addresses[i]['value'])

    try:
        select_index = int(input('Введите номер нужного вам адреса: ')) - 1
    except:
        return 1

    if select_index < 0 or select_index > len(list_addresses) / 2:
        return 2

    return list_addresses[select_index]


# function to get coordinates
def do_search():
    os.system('cls||clear')
    select_address = get_address()

    if type(select_address) == int:
        if select_address == 1:
            print('\nОшибка: введенное значение не является числом')
        elif select_address == 2:
            print('\nОшибка: введенное значение не входит в диапазон')
        else:
            print(f'\n{ErrorText}\n\nКод ошибки: {select_address}')
        print('Нажмите любую клавишу для продолжения')
        getch()
        return


    coords = api_requests.get_coords_on_query(select_address['fias_id'])
    print('\nВыбранный адрес: ' + select_address['value'] +
          '\nДолгота: ' + coords['lon'] +
          '\nШирота: ' + coords['lat'] +
          '\nНажмите любую клавишу для продолжения')
    getch()


def main():
    while True:
        os.system('cls||clear')
        print('Программа поиска координат по адресу\n'
              '1 - ввести адрес для поиска\n'
              '2 - настройки\n'
              '0 - выход')
        key = getch()
        if key == b'1':
            do_search()
        elif key == b'2':
            change_settings()
        elif key == b'0':
            break


if __name__ == "__main__":
    main()
