# Тестовое задание для UpTrader
___
## Установка и запуск
1. Проверить наличие poetry. Если нету, то уставновить командой вне виртуального окружения:
> pip install poetry
2. Выполнить команду:
> git clone https://github.com/DeadGEEK990/UpTraderTestTusk
3. Выполнить команду:
> cd UpTraderTestTusk
4. Установить зависимости:
> python -m poetry install
5. Выполнить миграцию:
> python -m poetry run python manage.py migrate
6. Создать суперпользователя (для входа в админку):
> python -m poetry run python manage.py createsuperuser
7. Запустить приложения:
> python -m poetry run python manage.py runserver
___
## Работа с проектом
При создании элементов меню в админке необходимо указывать название меню.
В данном проекте в шаблоне base.html (tree_menu/templates/base.html)
используется строка {% draw_menu 'main_menu' %}, где
"main_menu" название меню. При переходе на http://127.0.0.1:8000/tree/ будет отображено
древовидное меню со всеми эелментами, в которых название меню соответствовало "main_menu".
Соответственно можно создавать другие древовидные меню со своими названиями.
Пример заполнения элемента меню: 
___
Name: Меню1-ветка1 (такое название только для удобства отслеживания, можно использовать любое название
)\
Menu name: main_menu \
URL: https://exapmle.com \
Parent: -
___
Name: Меню1-ветка1-ветка1 \
Menu name: main_menu \
URL: https://exapmle.com \
Parent: Меню1-ветка1


