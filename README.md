Django Notes ORM

Простое приложение заметок на Django с PostgreSQL и Docker.

Возможности

Список пользователей

Детальная страница пользователя

Список заметок

Детальная страница заметки

Создание заметки

Админ-панель Django

Технологии

Python / Django

PostgreSQL

Docker / Docker Compose

Как запустить

Создайте файл .env:

POSTGRES_DB=notes_db
POSTGRES_USER=notes_user
POSTGRES_PASSWORD=notes_password
DB_HOST=db
DB_PORT=5432


Запустите проект:

docker-compose up --build


Примените миграции:

docker-compose exec web python manage.py migrate


Создайте суперпользователя:

docker-compose exec web python manage.py createsuperuser

Доступные страницы

Главная (список заметок):
http://localhost:8000/

Список пользователей:
http://localhost:8000/users/

Детальная страница пользователя:
http://localhost:8000/users/
<id>/

Детальная заметка:
http://localhost:8000/notes/
<id>/

Создание новой заметки:
http://localhost:8000/add_note/
 (если у тебя такая страница)

Админ-панель:
http://localhost:8000/admin