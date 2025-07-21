import psycopg2
from psycopg2 import sql
from dotenv import dotenv_values
from datetime import datetime

config = dotenv_values(".env")

DB_NAME = config.get("DB_NAME")
DB_USER = config.get("DB_USER")
DB_PASSWORD = config.get("DB_PASSWORD")
DB_HOST = config.get("DB_HOST", "localhost")
DB_PORT = config.get("DB_PORT", 5432)

def create_db():
    try:
        
        conn = psycopg2.connect(
            dbname="postgres",
            user=config['DB_USER'],
            password=config['DB_PASSWORD'],
            host=config.get('DB_HOST', 'localhost'),
            port=config.get('DB_PORT', 5432)
        )
        conn.autocommit = True
        cur = conn.cursor()

       
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (config['DB_NAME'],))
        exists = cur.fetchone()
        if not exists:
            cur.execute(f"CREATE DATABASE {config['DB_NAME']}")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Ошибка при создании БД: {e}")
        exit(1)


def connect_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def init_db():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT DEFAULT 'not added',
            category TEXT DEFAULT 'not added',
            deadline TEXT DEFAULT 'indefinitely',
            status BOOLEAN DEFAULT FALSE,
            date_created DATE DEFAULT CURRENT_DATE
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def list_tasks():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, status FROM tasks ORDER BY id, status;")
    tasks = cur.fetchall()
    if not tasks:
        print("Задач нет.")
    else:
        for task in tasks:
            status = "(completed)" if task[2] else "(pending)"
            print(f"{task[0]} | {task[1]} {status}")
    cur.close()
    conn.close()

def listall_for_func(func):
    def wrapper():
        list_tasks()
        func()
        list_tasks()
    return wrapper


@listall_for_func
def add_task():
    name = input("Название задачи: ").strip()
    description = input("Описание (Enter = не указано): ").strip() or "not added"
    category = input("Категория (Enter = не указано): ").strip() or "not added"
    deadline = input("Дедлайн (YYYY-MM-DD или Enter = без срока): ").strip() or "indefinitely"
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tasks (name, description, category, deadline)
        VALUES (%s, %s, %s, %s)
    """, (name, description, category, deadline))
    conn.commit()
    cur.close()
    conn.close()
    print("Задача добавлена.")



@listall_for_func
def delete_task():
    task_id = input("Какую задачу удалить [id]:")
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()

@listall_for_func
def toggle_task():
    task_id = input("Статус какой задачи обновить [id]:")
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        UPDATE tasks
        SET status = NOT status
        WHERE id = %s
    """, (task_id,))
    conn.commit()
    cur.close()
    conn.close()