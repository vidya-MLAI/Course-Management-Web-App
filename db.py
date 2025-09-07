import sqlite3

DB_NAME = "courses.db"

def init_db():
    """Initialize the database and create table if not exists"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            instructor TEXT,
            duration TEXT,
            fees TEXT,
            mode TEXT
        )
    """)
    conn.commit()
    conn.close()

def reset_db():
    """Reset the database (drops and recreates the courses table)"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS courses")
    conn.commit()
    conn.close()
    init_db()
    print("✅ Database reset successfully!")

# ---------------- CRUD Operations ----------------

def add_course(title, description, instructor, duration, fees, mode):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "INSERT INTO courses (title, description, instructor, duration, fees, mode) VALUES (?, ?, ?, ?, ?, ?)",
        (title, description, instructor, duration, fees, mode)
    )
    conn.commit()
    conn.close()

def get_courses():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM courses")
    courses = c.fetchall()
    conn.close()
    return courses

def update_course(course_id, title, description, instructor, duration, fees, mode):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        UPDATE courses 
        SET title=?, description=?, instructor=?, duration=?, fees=?, mode=?
        WHERE id=?
    """, (title, description, instructor, duration, fees, mode, course_id))
    conn.commit()
    conn.close()

def delete_course(course_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM courses WHERE id=?", (course_id,))
    conn.commit()
    conn.close()
