# Поисковик координат по адресу
Программа выполняет поиск координат по введенному адресу. По использует данные с сайта https://dadata.ru/
Функционал:
- поиск возможных вариантов по введенному адресу;
- вывод точных координат;
- настройка исходного адреса, ключа API, языка вывода (доступен русский и английский языки);
- сохранение настроек пользователя.

# Инструкция
При первом запуске программы необходимо ввести API ключ для доступа к Dadata.
Для выбора функций в программе используются нажатия цифр на клавиатуре.

При нажатии 1 выполняется основной функционал программы по поиску координат:
1. Введите желаемый адрес;
2. Программа предложит список из 10 возможных вариантов, введите номер нужного и нажмите Enter;
3. Вам отобразятся координаты выбранного адреса.

При нажатии 2 выполянется переход в меню настроек, в котором Вы можете настроить функционал:
- поменять базовый адрес;
- поменять API ключ;
- поменять язык вывода (ru/en, по умолчанию ru).
> Чтобы поменять адрес или API ключ выберите нужный параметр, введите новое значение и нажмите Enter. Чтобы изменить язык выберите соответствующий пункт и язык автоматически поменяется на противоположный

# Техническое
Сохранение настроек выполняется в файл settings_file.db в виде базы данных SQLite.

Список используемых библиотек хранится в файле requirements.txt
