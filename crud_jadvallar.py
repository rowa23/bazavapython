import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"  # <-- bu joyda o'z parolingizni yozing
)
cur = conn.cursor()

def add_employee():
    first = input("Ismi: ")
    last = input("Familiyasi: ")
    title = input("Lavozimi: ")
    city = input("Shahri: ")
    country = input("Davlati: ")

    cur.execute("""
        INSERT INTO employees (first_name, last_name, title, city, country)
        VALUES (%s, %s, %s, %s, %s)
    """, (first, last, title, city, country))
    conn.commit()
    print("Xodim qo‘shildi!\n")


def get_employees():
    cur.execute("SELECT employee_id, first_name, last_name, title, city, country FROM employees")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print()


def update_employee():
    emp_id = input("Tahrir qilinadigan xodim ID: ")
    city = input("Yangi shahar nomi: ")

    cur.execute("""
        UPDATE employees SET city = %s WHERE employee_id = %s
    """, (city, emp_id))
    conn.commit()
    print("Xodim ma’lumoti yangilandi!\n")


def delete_employee():
    emp_id = input("O‘chiriladigan xodim ID: ")
    cur.execute("DELETE FROM employees WHERE employee_id = %s", (emp_id,))
    conn.commit()
    print(" Xodim o‘chirildi!\n")

def order_detail():
    order_id = input("Order ID kiriting: ")
    cur.execute("""
        SELECT 
            o.order_id,
            o.order_date,
            c.company_name AS customer,
            e.first_name || ' ' || e.last_name AS employee,
            od.product_id,
            od.unit_price,
            od.quantity,
            od.discount
        FROM orders o
        JOIN order_details od ON o.order_id = od.order_id
        JOIN customers c ON o.customer_id = c.customer_id
        JOIN employees e ON o.employee_id = e.employee_id
        WHERE o.order_id = %s
    """, (order_id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print()


def orders_by_date():
    start_date = input("Boshlanish sanasi (YYYY-MM-DD): ")
    end_date = input("Tugash sanasi (YYYY-MM-DD): ")

    cur.execute("""
        SELECT order_id, order_date, customer_id, ship_city
        FROM orders
        WHERE order_date BETWEEN %s AND %s
        ORDER BY order_date
    """, (start_date, end_date))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print()

def main_menu():
    while True:
        print("""
1. Xodim qo‘shish
2. Xodimlarni ko‘rish
3. Xodimni tahrirlash
4. Xodimni o‘chirish
5. Order tafsiloti
6. Sana oralig‘idagi buyurtmalar
7. Chiqish
""")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            add_employee()
        elif tanlov == "2":
            get_employees()
        elif tanlov == "3":
            update_employee()
        elif tanlov == "4":
            delete_employee()
        elif tanlov == "5":
            order_detail()
        elif tanlov == "6":
            orders_by_date()
        elif tanlov == "7":
            print("Dastur tugadi.")
            break
        else:
            print("Noto‘g‘ri tanlov, qaytadan urinib ko‘ring.\n")

if __name__ == "__main__":
    main_menu()
    cur.close()
    conn.close()
