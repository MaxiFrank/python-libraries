import sqlite3


data = [
    ("John Doe", 30, "Software Engineer", "Engineering", "A"),
    ("Jane Smith", 35, "Data Scientist", "Analytics", "B"),
    ("Alice Johnson", 40, "Marketing Manager", "Marketing", "C"),
]

conn = sqlite3.connect("companydata.db")

cursor = conn.cursor()

create_table_query = """
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name text,
    age integer,
    title text, 
    department text,
    paygrade integer
    )
"""
cursor.execute(create_table_query)

for row in data:
    cursor.execute(
        "INSERT INTO employees (name, age, title, department, paygrade) VALUES (?, ?, ?, ?, ?)",
        row,
    )

conn.commit()
conn.close()

print(
    "Database 'employees.db' has been created successfully with the 'employees' table."
)
