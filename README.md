Task Manager CLI 

Описание:
Консольное Python-приложение для управления списком задач
с использованием PostgreSQL в качестве хранилища данных.
Позволяет добавлять, удалять, переключать статус задач и просматривать их.

---

Функции:

- Добавление новой задачи
- Удаление задачи по ID
- Переключение статуса задачи (выполнено / не выполнено)
- Просмотр всех задач
- Хранение данных в PostgreSQL
- .env-файл для конфиденциальных настроек

---

Установка:

0. Установите необходимые зависимости:
`pip install -r requirements.txt`

1. Создайте файл `.env` в корневой папке со следующим содержанием:
   
DB_NAME=tasks  
DB_USER=postgres  
DB_PASSWORD=your_password  
DB_HOST=localhost  
DB_PORT=5432  

2. Убедитесь, что PostgreSQL установлен и запущен.

3. Создайте базу данных:

Через psql:
    psql -U postgres -h localhost  
    CREATE DATABASE tasks;

Или через код:
    при первом запуске `main.py` база создастся автоматически, если её нет.

---

Запуск:

    python main.py

---

Команды CLI:

    add       — добавить новую задачу
    delete    — удалить задачу по ID
    update    — переключить статус (выполнено / не выполнено)
    listall   — показать все задачи
    help      — список команд
    stop      — выход из программы

---

Структура таблицы tasks:

CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT DEFAULT 'not added',
    category TEXT DEFAULT 'not added',
    deadline TEXT DEFAULT 'indefinitely',
    status BOOLEAN DEFAULT FALSE,
    date_created DATE DEFAULT CURRENT_DATE
);

---

Поддержка:

- Убедитесь, что PostgreSQL сервер запущен.
- Проверьте правильность данных подключения в `.env`.
- Убедитесь, что база данных `tasks` существует или используйте `create_database_if_not_exists()` перед `init_db()`.

Проект может быть расширен для работы через REST API, но по умолчанию ориентирован на удобную работу из терминала.
