# '''
# aiogram
# decorator, generator, iterator
# '''
# import time
# from
# yield
# [1, 2, 3, 4]

# for (python) foreach
# for (c++)

#
# from math import pow
#
# print(pow(2, 8))
#
# a = 2
# b = 'hello'
#
#
# def gen():
#     yield 1
#     yield 2
#     yield 3
#
#
# def result():
#     yield from gen()
#
#
# for i in result():
#     print(i)
#
#
# def decorator(func):
#     def wrapper(*args):
#         if any(map(lambda i: not isinstance(i, str), args)):
#             print('Warning')
#         # for i in args:
#         #     if not isinstance(i, str):
#         #         print('Warning')
#         #         break
#         return func(*args)
#
#     return wrapper
#
# @decorator
# def register(*args):
#     return args


# print(register('2', .32, '2'))

# keylarning eng maximal uzunligi 3 bolsin, keylilar str
# args - int, float, bool

#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         if any(map(lambda i: not isinstance(i, (int, float)), args)):
#             print('Warning')
#         elif any(map(lambda i: not (type(i) == str and len(i) < 4), kwargs.values())):
#             print('Warning')
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @decorator
# def register(*args, **kwargs):
#     return args, kwargs
#
#
# register(2, 3, 23.5, a='127')  # Warning
# register(2, 3.0, False, a='321')  # Warning
# register(2, 3, 23.5, a='1t7')  #
#

#
# class A:
#     pass
#
# class B(A):
#     pass
#
#
# a = A()
# b = B()
#
# print(isinstance(b, A))
# print(isinstance(b, A))

# numpy, pandas (Data Science, ML, AI, Data Engineering, Backend)
# async, multiprocessing (CPU), multithreading (IO)

# 1) matem tenglama 30min
# 2) download movie 30min

# 1 - processor, n ta thread
# 1 - thread, n ta async

# epoch time, unix time, posix time 1970-yil, 1-yanvar

# from threading import Thread
#
#
# def task(n):
#     time.sleep(4)
#     print(f'Task {n} bajarildi')
#
#
# start = time.time()
#
# oqimlar = []
# for i in range(10):
#     oqimlar.append(Thread(target=task, args=(i,), daemon=True))
#
# for oqim in oqimlar:
#     oqim.start()
#
# time.sleep(6)
#
# for oqim in oqimlar:
#     oqim.join()
#
#
# end = time.time()
# print(int(end - start), '- seconds')

#
# print(1)  # 10 min
# print(2)  # 10 min
# print(3)  # 10 min
# print(4)  # 10 min
# print(5)  # 10 min
#
# # 50 min

# '============================================================================================='


# import re
# import fitz
#
# pdf_file = "python-task.pdf"
# url_regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=\n]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
# with fitz.open(pdf_file) as file:
#     for page in file:
#         text = page.get_text()
#         for img in page.get_images():
#             rsm = img[0]
#             image = file.extract_image(rsm)
#             with open(f"{rsm}.{image['ext']}", "wb") as f:
#                 f.write(image["image"])
#     for match in re.finditer(url_regex, text):
#         url = match.group()
#         with open('links.txt', 'a') as f:
#             f.write(url + '\n')
#


# '================================================================================================'












