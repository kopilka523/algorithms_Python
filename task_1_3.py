"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для третьего скрипта
"""


from collections import Counter
from memory_profiler import memory_usage
from random import randint
from numpy import array


def decor(func):
    def wrapper():
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# @decor
# def func_1():
#     arr = [randint(1, 10) for _ in range(1000000)]
#     cnt = Counter(arr).most_common(1)
#     return f'Чаще всего встречается число {cnt[0][0]}, ' \
#            f'оно появилось в массиве {cnt[0][1]} раз(а)'
#
#
# if __name__ == '__main__':
#
#     res, mem_diff = func_1()
#     print(res)
#     print(mem_diff)  # 0.65625


@decor
def func_1():
    arr = array([randint(1, 10) for _ in range(1000000)])
    cnt = Counter(arr).most_common(1)
    return f'Чаще всего встречается число {cnt[0][0]}, ' \
           f'оно появилось в массиве {cnt[0][1]} раз(а)'


if __name__ == '__main__':

    res, mem_diff = func_1()
    print(res)
    print(mem_diff)  # 0.015625

#  Урок 4, задание 4 курса "Алгоритмы".
#  Использована функция array из модуля numpy для оптимизации использования памяти массивом.
#  Результат: 0.65625 против 0.015625 с использованием array.
