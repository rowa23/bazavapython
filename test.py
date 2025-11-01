# def decrator(func):
#     def wripper(*args,**kwargs):
#         print("Najot ta'lim o'quvchisi")
#         func(*args,**kwargs)
#         print("Yusupov Ravshan")
#     return wripper
#
# @decrator
# def salom():
#     print()
# salom()
#
# #yeild da 1 dan 10 gacha sonlarni qaytaradigan funksiya
# def sonlar():
#     for i in range(1, 11):
#         yield i
#
# for son in sonlar():
#     print(son)

# toq sonlarni kvadratini qaytaradigan itarator
# class toqsonlar:
#     def __init__(self, n):
#         self.n = n
#         self.current = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.current <= self.n:
#             son = self.current
#             self.current += 1
#             if son % 2 != 0:
#                 return son ** 2
#         raise StopIteration
#
# for son in toqsonlar(10):
#     print(son)
##
###
####
# 2. Getter va Setter nima?
# Getter → obyekt ichidagi qiymatni oladi (o‘qiydi)
# Setter → obyekt ichidagi qiymatni o‘zgartiradi (yozadi)
# Ammo ular to‘g‘ridan-to‘g‘ri ishlatilmaydi, balki maxsus usul bilan yaratiladi.
####
###
##
#
# class Talaba:
#     def __init__(self, ism):
#         self._ism = ism   # pastki chiziq → "himoyalangan" atribut
#
#     # getter
#     def get_ism(self):
#         return self._ism

    # setter
#     def set_ism(self, yangi_ism):
#         if yangi_ism.isalpha():    # faqat harflardan iborat bo‘lsa
#             self._ism = yangi_ism
#         else:
#             print("Ism faqat harflardan iborat bo‘lishi kerak!")
# t = Talaba("Ravshan")

# print(t.get_ism())    # getter chaqiriladi
# t.set_ism("Alisa")    #  setter chaqiriladi
# print(t.get_ism())
#
# t.set_ism("123")      # noto‘g‘ri qiymat


# class Student:
#     def __init__(self,ism):
#         self._ism=ism
#
#     def get_ism(self):
#         return self._ism
#
#
#     def set_ism(self):

# class Talaba:
#     def __init__(self, ism):
#         self._ism = ism
#
#     @property
#     def ism(self):          # getter
#         return self._ism
#
#     @ism.setter
#     def ism(self, qiymat):  # setter
#         if qiymat.isalpha():           # faqat harflar bo‘lsa
#             self._ism = qiymat
#         else:
#             print("Ism faqat harflardan iborat bo‘lishi kerak!")
#
#
# t = Talaba("Ravshan")
# print(t.ism)       # getter chaqiriladi
#
# t.ism = "Alisa"    #  to‘g‘ri
# print(t.ism)
#
# t.ism = "Alisa123" #  noto‘g‘ri, xabar chiqadi


# def f1(f):
#     def f2(*args,**kwargs):
#         print("boshlandi")
#         f(*args,**kwargs)
#         print("ali")
#     return f2
#
# @f1
# def salom():
#     print("dunyo")
# salom()
# ======================================================================================================



 # Generator -iterator qaytaruvchi funksiya bo’lib, iterator
# yaratishning oson yo’li hisoblanadi.
# 1-m
# def try_generator(y):
#     n = y
#     n += 1
#     print("bajarildi")
#     yield n
#
#     n *= 2
#     print("bajarildi 2")
#     yield n
#
#     n += 10
#     print("bajarildi 3")
#     yield n
# # #
# # # #
# result = try_generator(3)
# print(type(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(result)
# #
# for item in result:
#     print(item)
# #
def generator_manager(n):

    for i in range(1,n+1):
        yield i*i

# for i in generator_manager(10):
#     print(i)
# generator va for sikli:
# def for_gen(start, stop):
#     for i in range(start, stop):
#         yield i
# # #
# result = for_gen(1, 5)
# # #
# print(result)
# #
# for item in result:
#     print(item)
# def gen_for(a, b):
#     s = 0
#     for i in range(a, b, -1):
#         s += i
#         yield s
# r = gen_for(10,5)
# for item in r:
#     print(item)
# # Anonim generator yaratish
# my_list_com =  [num for num in range(1000)]
# print(my_list_com)

# my_generator = (num for num in range(10))
# print(my_generator)
# for i in my_generator:
#     print(i)

# class Counter:
#     def __init__(self, start, stop):
#         self.start = start - 1
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start < self.stop:
#             return self.start
#         raise StopIteration
#
#
# a = Counter(1, 10)
# for item in a:
#     print(item)

# a = (i for i in range(1, 100) if i % 5 == 0 and i % 2 == 1)
# # print(a)
# for i in a:
#     print(i, end=" ")