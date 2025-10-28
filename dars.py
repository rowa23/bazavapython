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
from functools import wraps

def count_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} ning ishlash vaqti: {end - start:.6f} soniya")
        return result
    return wrapper

@count_dec
def counter(n=100_000_000):
    count = 0
    for i in range(n):
        count += 1
    return count

if __name__ == "__main__":
    # demo: 1 million iteratsiya — tez va ko‘ringan natija beradi
    print("Natija:", counter(100_000_000))

