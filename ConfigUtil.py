# encoding:utf-8
import configparser
import os


def set_config(option, value):
    config = configparser.ConfigParser()
    config.read(os.getcwd() + '/resources/config/config.properties')
    config.set('position', option, str(value))
    with open(os.getcwd() + '/resources/config/config.properties', 'w') as op:
        config.write(op)


def get_config(option):
    config = configparser.ConfigParser()
    config.read(os.getcwd() + '/resources/config/config.properties')
    return int(config.get('position', option))
