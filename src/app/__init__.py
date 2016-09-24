# -*- coding: utf-8 -*-
from threading import Thread
from uuid import uuid4

import os
from flask import Flask, request, jsonify
import utils
from config import default


flask_app = Flask('test_web_server')
flask_app.config.from_object('config.default')


@flask_app.route('/api/number', methods=['GET'])
def plain_number():
    """
    Обработчик задачи полчения N-го простого числа,
    строковые аргументы: N - номер простого числа, которое должно быть получено
    :return: {'task_id': <task_id>} - id задачи, по которому может быть получен результат ее выполнения
    """
    try:
        number = int(request.args.get('N'))
    except ValueError:
        return 'Bad Value'
    task_id = uuid4()
    thread = Thread(target=utils.plain_number, args=(number, str(task_id)))
    thread.start()
    return jsonify({'task_id': task_id})


@flask_app.route('/api/factorization', methods=['GET'])
def factorization():
    """
    Обработчик задачи факторизации числа,
    строковые аргументы: N - число, которое должно быть разложено на простые сомножители
    :return: {'task_id': <task_id>} - id задачи, по которому может быть получен результат ее выполнения
    """
    try:
        number = int(request.args.get('N', 0))
    except ValueError:
        return 'Bad Value'
    task_id = uuid4()
    thread = Thread(target=utils.factorization, args=(number, str(task_id)))
    thread.start()
    return jsonify({'task_id': task_id})


@flask_app.route('/api/ping', methods=['GET'])
def ping():
    """
    Обработчик задачи пинга удаленного сервера,
    строковые аргументы: addr - адрес удаленного сервера, count - количество повторов вызова ping
    :return: {'task_id': <task_id>} - id задачи, по которому может быть получен результат ее выполнения
    """
    count = request.args.get('count', '1')
    addr = request.args.get('addr', '')
    if not addr:
        return 'No Address specified'
    task_id = uuid4()
    thread = Thread(target=utils.ping, args=(addr, count, str(task_id)))
    thread.start()
    return jsonify({'task_id': task_id})


@flask_app.route('/api/task_result', methods=['GET'])
def result():
    """
    Обработчик получения результата задачи
    Строковые параметры: task_id - id задачи, для которой должен быть получен результат
    :return: Если задача не готова, обработчик вернет строку 'Not Ready',
    Если задача выполнена будет возвращен результат выполнения задачи
    """
    task_id = request.args.get('task_id')
    result_file_path = os.path.join(default.PROJECT_DIR, 'app', 'temp_files', str(task_id))
    with open(result_file_path, 'rb') as fd:
        res = fd.read()
    os.remove(result_file_path)
    return res if res else 'Not Ready'
