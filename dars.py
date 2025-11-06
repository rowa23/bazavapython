# def my_detactor(func):
#     def wrapper(*args,**kwargs):
#         print("Funksiyadan oldin ishlayapti")
#         func(*args,**kwargs)
#         print("Funkdiyadan keyin ishlayapti")
#     return wrapper


# def f1(f):
#     def f2(*args,**kwargs):
#         print("ali")
#         f(*args,**kwargs)
#         print("vali")
#     return f2
#
# @f1
# def salom():
#     print("dunyo")
#
#
# salom()

import time
from ctypes import HRESULT
from functools import wraps

# def count_dec(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"{func.__name__} ning ishlash vaqti: {end - start:.6f} soniya")
#         return result
#     return wrapper
#
# @count_dec
# def counter(n=100_000_000):
#     count = 0
#     for i in range(n):
#         count += 1
#     return count
#
# if __name__ == "__main__":
#     # demo: 1 million iteratsiya — tez va ko‘ringan natija beradi
#     print("Natija:", counter(100_000_000))






# def  decarator(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start=time.perf_counter()
#         result=func(*args,**kwargs)
#         end=time.perf_counter()
#         print(f"{func.__name__} ishlash vaqti: {end:.6f} soniya")
#         return result
#     return wrapper
#
# @decarator
# def counter(n=10_000_000):
#     count=0
#     for i in range(n):
#         count+=1
#     return count
#
# if __name__=="__main__":
#     print("natija:", counter(10_000_000))

# import threading
# import time
#
# def ish(nomi):
#     for i in range(3):
#         print(f"{nomi} ishlayapti {i}")
#         time.sleep(1)
#
# # Ikki thread yaratamiz
# t1 = threading.Thread(target=ish, args=("Thread-1",))
# t2 = threading.Thread(target=ish, args=("Thread-2",))
#
# # Threadlarni ishga tushuramiz
# t1.start()
# t2.start()
#
# # Barcha threadlar tugaguncha kutamiz
# t1.join()
# t2.join()
#
# print("Barcha ishlar tugadi.")
#
# import time
#
# def hisobla(n):
#     return sum(range(n))
#
# boshlanish = time.time()
# hisobla(100_000_000)
# tugash = time.time()
#
# print("Oddiy versiya:", tugash - boshlanish, "sekund")

from contextlib import contextmanager

@contextmanager
def file_manager(file_name, mode):
    f=None
    try:
        if "." not in file_name:
            raise NameError
        print(f"Fayl '{file_name}' ochilyapti...")
        f=open(file_name,mode)
        yield f
    finally:
        if f:
            print(f"Fayl '{file_name}' yopilyapti...")
            f.close()

with file_manager('dars5.py','r') as file:
    f=file.read()
    print(f)







