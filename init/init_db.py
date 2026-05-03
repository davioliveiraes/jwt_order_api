import sqlite3
import os


def init_database():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "storage.db")
    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schema.sql")

    with open(schema_path, "r") as f:
        schema = f.read()

    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(schema)
        conn.commit()
        print(f"✓ Banco de dados inicializado em: {db_path}")
    finally:
        conn.close()


if __name__ == "__main__":
    init_database()