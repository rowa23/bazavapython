import psycopg2

conn = psycopg2.connect(
    dbname="news_db",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def add_department(title):
    cursor.execute("INSERT INTO department (title) VALUES (%s)", (title,))
    conn.commit()
    print("Department qo‘shildi.")

def view_departments():
    cursor.execute("SELECT * FROM department")
    departments = cursor.fetchall()
    print("\n DEPARTMENTLAR:")
    for d in departments:
        print(f"ID: {d[0]}, Title: {d[1]}")

def update_department(id, new_title):
    cursor.execute("UPDATE department SET title = %s WHERE id = %s", (new_title, id))
    conn.commit()
    print("Department yangilandi.")

def delete_department(id):
    cursor.execute("DELETE FROM department WHERE id = %s", (id,))
    conn.commit()
    print("Department o‘chirildi.")

def add_country(title, type_):
    cursor.execute("INSERT INTO country (title, type) VALUES (%s, %s)", (title, type_))
    conn.commit()
    print("Country qo‘shildi.")

def view_countries():
    cursor.execute("SELECT * FROM country")
    countries = cursor.fetchall()
    print("\nCOUNTRYLAR:")
    for c in countries:
        print(f"ID: {c[0]}, Title: {c[1]}, Type: {c[2]}")

def update_country(id, title, type_):
    cursor.execute("UPDATE country SET title = %s, type = %s WHERE id = %s", (title, type_, id))
    conn.commit()
    print("Country yangilandi.")

def delete_country(id):
    cursor.execute("DELETE FROM country WHERE id = %s", (id,))
    conn.commit()
    print("Country o‘chirildi.")

def add_employee(name, last_name, country_id, department_id, salary, email, phone):
    cursor.execute("""
        INSERT INTO employee (name, last_name, country_id, department_id, salary, email, phone)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (name, last_name, country_id, department_id, salary, email, phone))
    conn.commit()
    print("Hodim qo‘shildi.")

def view_employees():
    cursor.execute("""
        SELECT e.id, e.name, e.last_name, c.title AS country, d.title AS department, e.salary, e.email, e.phone
        FROM employee e
        JOIN country c ON e.country_id = c.id
        JOIN department d ON e.department_id = d.id
        ORDER BY e.id
    """)
    employees = cursor.fetchall()
    print("\nHODIMLAR:")
    for e in employees:
        print(f"ID: {e[0]}, {e[1]} {e[2]}, Country: {e[3]}, Dept: {e[4]}, Salary: {e[5]}, Email: {e[6]}, Phone: {e[7]}")

def update_employee(id, name, last_name, salary):
    cursor.execute("UPDATE employee SET name=%s, last_name=%s, salary=%s WHERE id=%s",
                   (name, last_name, salary, id))
    conn.commit()
    print("Hodim yangilandi.")

def delete_employee(id):
    cursor.execute("DELETE FROM employee WHERE id = %s", (id,))
    conn.commit()
    print("Hodim o‘chirildi.")

def menegerlarni_korish():
    print("\nmanagerlar:")
    cursor.execute("""SELECT d.title AS department, c.title AS country, COUNT(e.id) AS hodimlar_soni
        FROM employee e
        JOIN department d ON e.department_id = d.id
        JOIN country c ON e.country_id = c.id
        GROUP BY d.title, c.title
        ORDER BY d.title
    """)
    result = cursor.fetchall()
    for row in result:
        print(f"Departament: {row[0]}, Country: {row[1]}, Hodimlar soni: {row[2]}")

def department_menu():
    while True:
        print("DEPARTMENT\n1.Qo‘shish\n2.Ko‘rish\n3.Tahrirlash\n4.O‘chirish\n5.Orqaga")
        ch = input("Tanlang: ")
        if ch == "1":
            t = input("Department nomi: ")
            add_department(t)
        elif ch == "2":
            view_departments()
        elif ch == "3":
            i = input("ID: ")
            nt = input("Yangi nom: ")
            update_department(i, nt)
        elif ch == "4":
            i = input("ID: ")
            delete_department(i)
        elif ch == "5":
            break

def country_menu():
    while True:
        print("Country\n1.Qo‘shish\n2.Ko‘rish\n3.Tahrirlash\n4.O‘chirish\n5.Orqaga")
        ch = input("Tanlang: ")
        if ch == "1":
            t = input("Country nomi: ")
            ty = input("Turi: ")
            add_country(t, ty)
        elif ch == "2":
            view_countries()
        elif ch == "3":
            i = input("ID: ")
            t = input("Yangi nom: ")
            ty = input("Yangi turi: ")
            update_country(i, t, ty)
        elif ch == "4":
            i = input("ID: ")
            delete_country(i)
        elif ch == "0":
            break

def employee_menu():
    while True:
        print("employee jadvali:\n1.Qo‘shish\n2.Ko‘rish\n3.Tahrirlash\n4.O‘chirish\n5.Orqaga")
        ch = input("Tanlang: ")
        if ch == "1":
            n = input("Ismi: ")
            l = input("Familiyasi: ")
            c = input("Country ID: ")
            d = input("Department ID: ")
            s = input("Maoshi: ")
            e = input("Email: ")
            p = input("Telefon: ")
            add_employee(n, l, c, d, s, e, p)
        elif ch == "2":
            view_employees()
        elif ch == "3":
            i = input("ID: ")
            n = input("Yangi ism: ")
            l = input("Yangi familiya: ")
            s = input("Yangi maosh: ")
            update_employee(i, n, l, s)
        elif ch == "4":
            i = input("ID: ")
            delete_employee(i)
        elif ch == "5":
            break

def main_menu():
    while True:
        print("ASOSIY MENYU:\n1.Department CRUD\n2.Country CRUD\n3.Employee CRUD\n4.Menegerlarni ko‘rish\n5.Chiqish")
        tanlov = input("Tanlang: ")
        if tanlov == "1":
            department_menu()
        elif tanlov == "2":
            country_menu()
        elif tanlov == "3":
            employee_menu()
        elif tanlov == "4":
            menegerlarni_korish()
        elif tanlov == "5":
            print("Dastur tugatildi.")
            break
        else:
            print("Noto‘g‘ri tanlov.")

if __name__ == "__main__":
    main_menu()
    cursor.close()
    conn.close()
