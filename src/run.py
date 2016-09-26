# -*- coding: utf-8 -*-
import os

from app import flask_app
from config import default


def main():
    # threaded = True  для организации доступа к серверу нескольких клиентов
    temp_dir = os.path.join(default.PROJECT_DIR, 'app', 'temp_files')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    flask_app.run(host='0.0.0.0', threaded=True)


if __name__ == '__main__':
    main()
