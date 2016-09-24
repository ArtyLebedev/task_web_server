# -*- coding: utf-8 -*-
import os

# Конфига почти нет,в данной задаче удалось обойтись стандартными настройками


class BaseConfig(object):
    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

default = BaseConfig
