# import psycopg2
# #
# # conn = psycopg2.connect(
# #     dbname="news_db",
# #     user="postgres",
# #     password="123",
# #     host="localhost",
# #     port="5432"
# # )
# # cursor = conn.cursor()
# #
# # def add_department(title):
# #     cursor.execute("INSERT INTO department (title) VALUES (%s)", (title,))
# #     conn.commit()
# #     print("Department qo‘shildi.")
# #
# # def view_departments():
# #     cursor.execute("SELECT * FROM department")
# #     departments = cursor.fetchall()
# #     print("\n DEPARTMENTLAR:")
# #     for d in departments:
# #         print(f"ID: {d[0]}, Title: {d[1]}")
# #
# # def update_department(id, new_title):
# #     cursor.execute("UPDATE department SET title = %s WHERE id = %s", (new_title, id))
# #     conn.commit()
# #     print("Department yangilandi.")
# #
# # def delete_department(id):
# #     cursor.execute("DELETE FROM department WHERE id = %s", (id,))
# #     conn.commit()
# #     print("Department o‘chirildi.")
# #
# # def add_country(title, type_):
# #     cursor.execute("INSERT INTO country (title, type) VALUES (%s, %s)", (title, type_))
# #     conn.commit()
# #     print("Country qo‘shildi.")
# #
# # def view_countries():
# #     cursor.execute("SELECT * FROM country")
# #     countries = cursor.fetchall()
# #     print("\nCOUNTRYLAR:")
# #     for c in countries:
# #         print(f"ID: {c[0]}, Title: {c[1]}, Type: {c[2]}")
# #
# # def update_country(id, title, type_):
# #     cursor.execute("UPDATE country SET title = %s, type = %s WHERE id = %s", (title, type_, id))
# #     conn.commit()
# #     print("Country yangilandi.")
# #
# # def delete_country(id):
# #     cursor.execute("DELETE FROM country WHERE id = %s", (id,))
# #     conn.commit()
# #     print("Country o‘chirildi.")
# #
# # def add_employee(name, last_name, country_id, department_id, salary, email, phone):
# #     cursor.execute("""
# #         INSERT INTO employee (name, last_name, country_id, department_id, salary, email, phone)
# #         VALUES (%s, %s, %s, %s, %s, %s, %s)
# #     """, (name, last_name, country_id, department_id, salary, email, phone))
# #     conn.commit()
# #     print("Hodim qo‘shildi.")
# #
# # def view_employees():
# #     cursor.execute("""
# #         SELECT e.id, e.name, e.last_name, c.title AS country, d.title AS department, e.salary, e.email, e.phone
# #         FROM employee e
# #         JOIN country c ON e.country_id = c.id
# #         JOIN department d ON e.department_id = d.id
# #         ORDER BY e.id
# #     """)
# #     employees = cursor.fetchall()
# #     print("\nHODIMLAR:")
# #     for e in employees:
# #         print(f"ID: {e[0]}, {e[1]} {e[2]}, Country: {e[3]}, Dept: {e[4]}, Salary: {e[5]}, Email: {e[6]}, Phone: {e[7]}")
# #
# # def update_employee(id, name, last_name, salary):
# #     cursor.execute("UPDATE employee SET name=%s, last_name=%s, salary=%s WHERE id=%s",
# #                    (name, last_name, salary, id))
# #     conn.commit()
# #     print("Hodim yangilandi.")
# #
# # def delete_employee(id):
# #     cursor.execute("DELETE FROM employee WHERE id = %s", (id,))
# #     conn.commit()
# #     print("Hodim o‘chirildi.")
# #
# # def menegerlarni_korish():
# #     print("\nmanagerlar:")
# #     cursor.execute("""SELECT d.title AS department, c.title AS country, COUNT(e.id) AS hodimlar_soni
# #         FROM employee e
# #         JOIN department d ON e.department_id = d.id
# #         JOIN country c ON e.country_id = c.id
# #         GROUP BY d.title, c.title
# #         ORDER BY d.title
# #     """)
# #     result = cursor.fetchall()
# #     for row in result:
# #         print(f"Departament: {row[0]}, Country: {row[1]}, Hodimlar soni: {row[2]}")
# #
# # def department_menu():
# #     while True:
# #         print("DEPARTMENT\n1.Qo‘shish\n2.Ko‘rish\n3.Tahrirlash\n4.O‘chirish\n5.Orqaga")
# #         ch = input("Tanlang: ")
# #         if ch == "1":
# #             t = input("Department nomi: ")
# #             add_department(t)
# #         elif ch == "2":
# #             view_departments()
# #         elif ch == "3":
# #             i = input("ID: ")
# #             nt = input("Yangi nom: ")
# #             update_department(i, nt)
# #         elif ch == "4":
# #             i = input("ID: ")
# #             delete_department(i)
# #         elif ch == "5":
# #             break
# #
# # def country_menu():
# #     while True:
# #         print("Country\n1.Qo‘shish\n2.Ko‘rish\n3.Tahrirlash\n4.O‘chirish\n5.Orqaga")
# #         ch = input("Tanlang: ")
# #         if ch == "1":
# #             t = input("Country nomi: ")
# #             ty = input("Turi: ")
# #             add_country(t, ty)
# #         elif ch == "2":
# #             view_countries()
# #         elif ch == "3":
# #             i = input("ID: ")
# #             t = input("Yangi nom: ")
# #             ty = input("Yangi turi: ")
# #             update_country(i, t, ty)
# #         elif ch == "4":
# #             i = input("ID: ")
# #             delete_country(i)
# #         elif ch == "0":
# #             break
# #
# # def employee_menu():
# #     while True:
# #         print("employee jadvali:\n1.Qo‘shish\n2.Ko‘rish\n3.Tahrirlash\n4.O‘chirish\n5.Orqaga")
# #         ch = input("Tanlang: ")
# #         if ch == "1":
# #             n = input("Ismi: ")
# #             l = input("Familiyasi: ")
# #             c = input("Country ID: ")
# #             d = input("Department ID: ")
# #             s = input("Maoshi: ")
# #             e = input("Email: ")
# #             p = input("Telefon: ")
# #             add_employee(n, l, c, d, s, e, p)
# #         elif ch == "2":
# #             view_employees()
# #         elif ch == "3":
# #             i = input("ID: ")
# #             n = input("Yangi ism: ")
# #             l = input("Yangi familiya: ")
# #             s = input("Yangi maosh: ")
# #             update_employee(i, n, l, s)
# #         elif ch == "4":
# #             i = input("ID: ")
# #             delete_employee(i)
# #         elif ch == "5":
# #             break
# #
# # def main_menu():
# #     while True:
# #         print("ASOSIY MENYU:\n1.Department CRUD\n2.Country CRUD\n3.Employee CRUD\n4.Menegerlarni ko‘rish\n5.Chiqish")
# #         tanlov = input("Tanlang: ")
# #         if tanlov == "1":
# #             department_menu()
# #         elif tanlov == "2":
# #             country_menu()
# #         elif tanlov == "3":
# #             employee_menu()
# #         elif tanlov == "4":
# #             menegerlarni_korish()
# #         elif tanlov == "5":
# #             print("Dastur tugatildi.")
# #             break
# #         else:
# #             print("Noto‘g‘ri tanlov.")
# #
# # if __name__ == "__main__":
# #     main_menu()
# #     cursor.close()
# #     conn.close()
#
#
#
#
# from datetime import date
#
# # 🔹 Bazaga ulanamiz
# conn = psycopg2.connect(
#     host="localhost",
#     database="postgres",
#     user="postgres",
#     password="123"  # <-- bu joyda o'z parolingizni yozing
# )
# cur = conn.cursor()
#
#
# # =====================================================
# # 🧑‍💼 EMPLOYEES CRUD
# # =====================================================
# def add_employee():
#     first = input("Ismi: ")
#     last = input("Familiyasi: ")
#     title = input("Lavozimi: ")
#     city = input("Shahri: ")
#     country = input("Davlati: ")
#
#     cur.execute("""
#         INSERT INTO employees (first_name, last_name, title, city, country)
#         VALUES (%s, %s, %s, %s, %s)
#     """, (first, last, title, city, country))
#     conn.commit()
#     print("✅ Xodim qo‘shildi!\n")
#
#
# def get_employees():
#     cur.execute("SELECT employee_id, first_name, last_name, title, city, country FROM employees")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     print()
#
#
# def update_employee():
#     emp_id = input("Tahrir qilinadigan xodim ID: ")
#     city = input("Yangi shahar nomi: ")
#
#     cur.execute("""
#         UPDATE employees SET city = %s WHERE employee_id = %s
#     """, (city, emp_id))
#     conn.commit()
#     print("✏️ Xodim ma’lumoti yangilandi!\n")
#
#
# def delete_employee():
#     emp_id = input("O‘chiriladigan xodim ID: ")
#     cur.execute("DELETE FROM employees WHERE employee_id = %s", (emp_id,))
#     conn.commit()
#     print("🗑️ Xodim o‘chirildi!\n")
#
#
# # =====================================================
# # 📦 ORDERS FUNKSIYALARI
# # =====================================================
# def order_detail():
#     order_id = input("Order ID kiriting: ")
#     cur.execute("""
#         SELECT
#             o.order_id,
#             o.order_date,
#             c.company_name AS customer,
#             e.first_name || ' ' || e.last_name AS employee,
#             od.product_id,
#             od.unit_price,
#             od.quantity,
#             od.discount
#         FROM orders o
#         JOIN order_details od ON o.order_id = od.order_id
#         JOIN customers c ON o.customer_id = c.customer_id
#         JOIN employees e ON o.employee_id = e.employee_id
#         WHERE o.order_id = %s
#     """, (order_id,))
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     print()
#
#
# def orders_by_date():
#     start_date = input("Boshlanish sanasi (YYYY-MM-DD): ")
#     end_date = input("Tugash sanasi (YYYY-MM-DD): ")
#
#     cur.execute("""
#         SELECT order_id, order_date, customer_id, ship_city
#         FROM orders
#         WHERE order_date BETWEEN %s AND %s
#         ORDER BY order_date
#     """, (start_date, end_date))
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#     print()
#
#
# # =====================================================
# # 🔘 ASOSIY MENYU
# # =====================================================
# def main_menu():
#     while True:
#         print("""
# ========= MENYU =========
# 1. Xodim qo‘shish
# 2. Xodimlarni ko‘rish
# 3. Xodimni tahrirlash
# 4. Xodimni o‘chirish
# 5. Order tafsiloti (order_detail)
# 6. Sana oralig‘idagi buyurtmalar (orders_by_date)
# 0. Chiqish
# """)
#         tanlov = input("Tanlang (0-6): ")
#
#         if tanlov == "1":
#             add_employee()
#         elif tanlov == "2":
#             get_employees()
#         elif tanlov == "3":
#             update_employee()
#         elif tanlov == "4":
#             delete_employee()
#         elif tanlov == "5":
#             order_detail()
#         elif tanlov == "6":
#             orders_by_date()
#         elif tanlov == "0":
#             print("👋 Dastur tugadi.")
#             break
#         else:
#             print("⚠️ Noto‘g‘ri tanlov, qaytadan urinib ko‘ring.\n")
#
# if __name__ == "__main__":
#     main_menu()
#     cur.close()
#     conn.close()



# a = [1, 2, 3]
# b = a  # bu yerda yangi ro‘yxat yaratilmaydi
#
# b.append(4)
#
# print(a)  # [1, 2, 3, 4]
# print(b)  # [1, 2, 3, 4]


# import copy
#
# a = [[1, 2], [3, 4]]
# b = copy.copy(a)
#
# b[0].append(9)
#
# print(a)  # [[1, 2, 9], [3, 4]]
# print(b)  # [[1, 2, 9], [3, 4]]


# import copy
#
# a = [[1, 2], [3, 4]]
# b = copy.deepcopy(a)
#
# b[0].append(9)
#
# print(a)  # [[1, 2], [3, 4]]
# print(b)  # [[1, 2, 9], [3, 4]]
