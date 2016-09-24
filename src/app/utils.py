# -*- coding: utf-8 -*-
from subprocess import Popen

import os
from config import default


def plain_number(num, task_id):
    """
    Фунция для вычисления N-го по счету простого числа
    :param num: Номер простого числа
    :param task_id: id задачи, в файле с таким id будет хранится результат выполнения задачи
    :return: Int - N-ое простое число, например для входного номера 3 ответ будет - 5
    """
    if num < 1:
        return 0

    numbers = [2]
    i = 3
    while len(numbers) < num:
        if i % 10 == 5 and i > 10:
            i += 2
            continue

        for j in numbers:
            if j * j - 1 > i:
                numbers.append(i)
                break
            if not i % j:
                break
        else:
            numbers.append(i)
        i += 2

    with open(os.path.join(default.PROJECT_DIR, 'app', 'temp_files', task_id), 'wb') as fd:
        fd.write(str(numbers[-1]))

    return numbers[-1]


def factorization(num, task_id):
    """
    Фунция для факторизации числа
    :param num: Число, которое необходимо разложить на простые сомножители
    :param task_id: id задачи, в файле с названием id задачи будет храниться результат ее выполнения
    :return: List, в котром содержатся все простые множители числа, например для входного числа 15,
    возвращаемое значение будет равно [3, 5]
    """
    res = []
    num2 = num

    while num2 != 1:
        for i in xrange(2, num2 + 1):
            if num2 % i == 0:
                res.append(i)
                num2 /= i
                break

    with open(os.path.join(default.PROJECT_DIR, 'app', 'temp_files', task_id), 'wb') as fd:
        fd.write(str(res))

    return res


def ping(host, count, task_id):
    """
    Функция для пинга удаленного сервера
    :param host: Адрес сервера, который будет пинговаться
    :param count: Число вызовов функции ping
    :param task_id: id задачи, в файле с данным id будет храниться результат выполнения
    :return: "success"
    """
    result_file = os.path.join(default.PROJECT_DIR, 'app', 'temp_files', task_id)
    fd = open(result_file, 'wb')
    Popen(['ping', '-c', str(count), host], stdout=fd)
    fd.close()
    # output, _ = p.communicate(b"input data that is passed to subprocess' stdin")
    return 'success'
