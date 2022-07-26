import os
import sqlite3
from msvcrt import getch

url = 'https://suggestions.dadata.ru/'  # url to access to API
token: str  # API key
language = 'ru'  # language for response
content_type = 'application/json'  # type of response content
settings_file_name = 'settings_file.db'  # file name for settings
global sql_connection

# function to create a settings file (if it is missing)
def create_settings_file():
    global sql_connection, token
    try:
        token = input('Введите API ключ: ')
        sql_connection = sqlite3.connect(settings_file_name)
        sql_cursor = sql_connection.cursor()

        sql_query = 'CREATE TABLE settings (url TEXT, token TEXT, language TEXT)'
        sql_cursor.execute(sql_query)

        sql_query = f'INSERT INTO settings VALUES (\'{url}\', \'{token}\', \'{language}\')'
        sql_cursor.execute(sql_query)

        sql_cursor.close()
        sql_connection.commit()
    except:
        print("Ошибка создания файла настроек\n"
              "Нажмите любую клавишу для продолжения")
        getch()
    finally:
        if sql_connection:
            sql_connection.close()


# function of opening a settings file (if it exists)
def load_settings_file():
    global sql_connection, token, url, language
    try:
        sql_connection = sqlite3.connect(settings_file_name)
        sql_cursor = sql_connection.cursor()

        sql_query = "SELECT * FROM settings;"
        sql_cursor.execute(sql_query)
        record = sql_cursor.fetchone()

        url = record[0]
        token = record[1]
        language = record[2]

        sql_cursor.close()
    except:
        print("Ошибка чтения файла настроек\n"
              "Нажмите любую клавишу для продолжения")
        getch()
    finally:
        if sql_connection:
            sql_connection.close()


# function to save settings
def save_settings():
    global sql_connection
    try:
        sql_connection = sqlite3.connect(settings_file_name)
        sql_cursor = sql_connection.cursor()

        sql_query = f'UPDATE settings SET ' \
                    f'url = \'{url}\',' \
                    f'token = \'{token}\',' \
                    f'language = \'{language}\';'
        sql_cursor.execute(sql_query)

        sql_cursor.close()
        sql_connection.commit()

        print('Новые настройки успешно сохранены')
        getch()
    except:
        print("Ошибка сохранения настроек\n"
              "Нажмите любую клавишу для продолжения")
        getch()
    finally:
        if sql_connection:
            sql_connection.close()


# function to change settings
def change():
    global url, token, language
    while True:
        os.system('cls||clear')
        print(f'Текущие настройки:\n'
              f'1. Базовый URL: {url} \n'
              f'2. API ключ: {token}\n'
              f'3. Язык: {language} (доступно ru и en)\n'
              f'0. Назад\n'
              f'Чтобы изменить параметр нажмите выберите соответствующий номер')
        key = getch()
        if key == b'1':
            url = input('Введите новый адрес: ')
            save_settings()
        elif key == b'2':
            token = input('Введите новый API ключ: ')
            save_settings()
        elif key == b'3':
            if language == 'ru':
                language = 'en'
            else:
                language = 'ru'
            save_settings()
        elif key == b'0':
            break


# initialize settings function
def init():
    if os.path.exists(settings_file_name) == False:
        create_settings_file()
    else:
        load_settings_file()


if __name__ == "__main__":
    init()
