# Notes App (Django + Docker)

Простое приложение для заметок, созданное на Django.
Поддерживает категории, авторов, статусы и CRUD‑операции (создание, просмотр, редактирование, удаление заметок).
Проект полностью работает в Docker.

## Технологии проекта

* **Python 3.10**
* **Django 5**
* **PostgreSQL 15**
* **Docker & Docker Compose**
* **HTML / Django Templates**
* **Bootstrap (если используется)**
* **Git / GitHub**

---

## Запуск проекта

### 1. Установите Docker и Docker Compose

Если они не установлены, скачайте их с официального сайта Docker.

### 2. Клонируйте репозиторий

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <project-folder>
```

### 3. Запустите проект

```bash
docker compose up --build
```

После сборки приложение будет доступно по адресу:

```
http://localhost:8000/
```

---

## Миграции

Если нужно вручную создать или применить миграции:

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

---

## Основной функционал

* Создание заметки
* Просмотр списка заметок
* Детальная страница
* Удаление заметки
* Категории заметок
* Авторы заметок
* Статусы заметок

---

## Структура проекта

```
project/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
│
├── notes/               # Django‑проект
├── notes_app/           # Основное приложение
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
└── README.md
```

