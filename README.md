

# 📘 **Tudu — FastAPI ToDo App**

Асинхронное приложение задач с авторизацией через JWT (cookie), PostgreSQL и FastAPI.

---

## 🚀 Возможности

* Регистрация / Логин
* Хеширование паролей (bcrypt)
* JWT-токен в HttpOnly cookie
* Работа с задачами (создание, получение, удаление)
* Асинхронный стек: FastAPI + SQLAlchemy 2.0 + asyncpg
* Pydantic v2
* Poetry как менеджер зависимостей

---

# 📁 **Структура проекта**

```
tudu/
│
├── app/
│   ├── routers/           # эндпоинты auth/tasks
│   ├── models/            # SQLAlchemy ORM-модели
│   ├── schemas/           # Pydantic-схемы
│   ├── repositories/      # Работа с базой
│   ├── engines/           # PostgresEngine
│   ├── auth/              # JWT, hashing, dependencies
│   ├── settings.py        # загрузка ENV
│   └── main.py            # точка входа FastAPI
│
├── static/                # фронтенд HTML/JS
├── .env                   # конфигурация БД и JWT
├── pyproject.toml         # Poetry зависимости
├── .gitignore             # Неотслеживаемые гитом файлы
└── README.md              # этот файл
```

---

# 🛠 **1. Требования**

* Python **3.13+**
* Poetry **1.7+**
* PostgreSQL **14+**

---

# ⚙️ **2. Настройка окружения**

## 2.1. Клонировать проект

```bash
git clone https://github.com/Powarar/tudu.git
cd tudu
```

## 2.2. Установить зависимости

```bash
poetry install
```

## 2.3. Активировать виртуальное окружение Poetry

```bash
poetry env activate
```

---

# 🔧 **3. Конфигурация (.env)**

В корне проекта должен быть `.env`:

```
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_NAME=TUDU
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password

SECRET_KEY=your_key
ALGORITHM=HS256
```

## 📌 Как работает загрузка .env

В `Settings` прописано:

```python
model_config = SettingsConfigDict(
    env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
)

# 🗄 **4. Настройка PostgreSQL**

Создайте базу данных:

### Linux / macOS:

```bash
sudo -u postgres psql -c "CREATE DATABASE TUDU;"
```

### Windows (psql):

```bash
psql -U postgres -c "CREATE DATABASE TUDU;"
```

Проверь доступ:

```bash
psql -U postgres -d TUDU -c "\dt"
```

---

# ▶️ **5. Запуск приложения**

```bash
poetry run uvicorn app.main:app --reload
```

По умолчанию сервер поднимется на:

```
http://127.0.0.1:8000
```

---

# 🌐 **6. Фронтенд**

Открыть файл:

```
/static/index.html
```

или перейти в браузере:

```
http://127.0.0.1:8000/static/index.html
```

Фронт полностью написан на чистом HTML+JS.


# 📡 **7. Эндпоинты (API)**

## 🔐 Авторизация

### Регистрация

`POST /auth/register`

Body:

```json
{
  "username": "ivan",
  "first_name": "Иван",
  "last_name": "Иванов",
  "password": "password123"
}
```

### Логин

`POST /auth/login`

Сервер отправляет cookie:
`users_access_token=<JWT>`

---

## 📝 Задачи

### Получить задачи

`GET /tasks/`
(требует авторизацию)

### Создать задачу

`POST /tasks/`

```json
{
  "title": "Купить хлеб",
  "description": "вечером"
}
```

### Удалить задачу

`DELETE /tasks/{id}`

---
Первая рабочая версия. Могут быть ошибки из-за валидации в схемах. Фронтенд навайбкоден)