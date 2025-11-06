# def generator(a):
#     for i in range(1,a+1):
#         yield i*i
#
# for i in generator(5):
#         print(i)

# class Counter:
#     def __init__(self, low, high):
#         self.current = low - 1
#         self.high = high
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current += 1
#
#         if self.current < self.high:
#             return self.current
#         raise StopIteration
# class Counter:
#     def __init__(self, start, stop):
#         self.start = start + 1
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start -= 1
#
#         if self.start > self.stop:
#             return self.start
#         raise StopIteration
# #
# for elem in Counter(10, -10):
#     print(elem)
# # print(type(Counter(1, 10)))

# =====================================================================================================================
import sqlite3

conn = sqlite3.connect("database.db")  # Agar fayl bo‘lmasa, avtomatik yaratiladi
cur = conn.cursor()  # Kursor obyektini yaratamiz

s1 = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
"""
s12="""
insert into users(name,age) 
values ('ali1',21),('ali2',12);
"""

s2="SELECT * FROM users"
conn.commit()  # O‘zgarishlarni saqlash

cur.execute(s1)
# cur.executescript(s12) # malumot Qo'shish
print("bajarildi")
# rows = cur.fetchall()  # Natijalarni olish
# print(rows)
# for row in rows:

    # print(row)  # Har bir qatorni chiqarish
cur.close()
conn.close()

# class Student:
#     school = "IT Academy"
#
#     def __init__(self, name):
#         self.name = name
#
#     def show_name(self):
#         print("O‘quvchi:", self.name)
#
#     @classmethod
#     def show_school(cls):
#         print("Maktab:", cls.school)


# def decorator(func):
#     def salom():
#         print("salom")
#         func()
#         print("Yusupov")
#     return salom
#
# @decorator
# def salom_ber():
#     print("ravshan")
#
# salom_ber()


















