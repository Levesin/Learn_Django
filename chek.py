import psycopg2
from datetime import datetime

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="django_db",
    user="django_user",
    password="SEzHcAz73degvDxh36BypFePXsTBJKWY",
    host="localhost",
    port="5432"
)

# Создание курсора
cur = conn.cursor()

try:
    # SQL-запрос для добавления данных в таблицу "contacts_contact"
    sql = """INSERT INTO contacts_contact (name, phone, created_at, modified_at, is_auto_generated)
             VALUES (%s, %s, %s, %s, %s)"""

    # Параметры для запроса
    name = "John Doe"
    phone = 1234567890
    created_at = datetime.now()
    modified_at = datetime.now()
    is_auto_generated = False

    # Выполнение SQL-запроса
    cur.execute(sql, (name, phone, created_at, modified_at, is_auto_generated))

    # Подтверждение транзакции
    conn.commit()

    print("Данные успешно добавлены в базу данных!")

except (Exception, psycopg2.Error) as error:
    print("Ошибка при добавлении данных в базу данных:", error)

finally:
    # Закрытие курсора и соединения с базой данных
    if cur:
        cur.close()
    if conn:
        conn.close()
