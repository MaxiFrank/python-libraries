from collections import namedtuple
import csv
import sqlite3

EmployeeRecord = namedtuple("EmployeeRecord", "name, age, title, department, paygrade")


def basic_example():
    Point = namedtuple("Point", ["x", "y"])
    p = Point(11, 22)
    print("p.x + p.y = ", p.x + p.y)
    x, y = p
    print("x = ", x, "y = ", y)
    print("p is ", p)


def use_with_csv():
    for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "r"))):
        print(emp.name, emp.title)


def use_with_sqlite3():
    EmployeeRecord = namedtuple(
        "EmployeeRecord", "name, age, title, department, paygrade"
    )
    conn = sqlite3.connect("companydata.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, title, department, paygrade FROM employees")
    for emp in map(EmployeeRecord._make, cursor.fetchall()):
        print(emp.name, emp.title)


if "__main__" == __name__:
    basic_example()
    use_with_csv()
    use_with_sqlite3()
