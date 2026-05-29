import sqlite3

# Путь к твоей базе данных
db_path = 'db.sqlite3'

def create_tables():
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Создаем таблицу классов
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS school_classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT NOT NULL,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES auth_user (id)
        );
        """)

        # Создаем таблицу учеников
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            class_id INTEGER,
            birth_date TEXT,
            FOREIGN KEY (class_id) REFERENCES school_classes (id)
        );
        """)

        # Добавим один тестовый класс, чтобы список не был пустым
        cursor.execute("INSERT INTO school_classes (class_name) VALUES ('8-Б')")

        conn.commit()
        print("✅ Таблицы успешно созданы! Теперь можно делать сайт.")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_tables()