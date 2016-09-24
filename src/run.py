# -*- coding: utf-8 -*-

from app import flask_app


def main():
    # threaded = True  для организации доступа к серверу нескольких клиентов
    flask_app.run(host='0.0.0.0', threaded=True)


if __name__ == '__main__':
    main()
