#Decarator yaratish
#
#
# def decrator(func):
#     def wripper(*args,**kwargs):
#         func(*args,**kwargs)
#         print("salom")
#     return wripper
#
#
# @decrator
# def salom():
#     print("Ravshan")
# salom()
# import asyncio
# #Threading yaratish
#
# import time, os
# from threading import Thread, current_thread
# from multiprocessing import Process, current_process
#
# async  def f1():
#     print("f1 boshlandi")
#     await asyncio.sleep(3)
#     print("f1 tugadi")
#
# async  def f2():
#     print("f2 boshlandi")
#     await asyncio.sleep(3)
#     print("f2 tugadi")
#
# async  def f3():
#     await asyncio.gather(f1(),f2())
#
# asyncio.run(f2())
# def f01():
#     print("f01 boshlandi")
#     time.sleep(5)
#     print("f01 tugadi")