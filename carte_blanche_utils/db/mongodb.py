'''
========================================================
Mongo DB Utilities
--------------------------------------------------------
'''
import os
from pymongo import MongoClient

DB_URI = os.environ.get('MONGO_DB_URI', '127.0.0.1')
DB_PORT = os.environ.get('MONGO_DB_PORT', '27017')


def raw_connection(connection_args={}):
    '''
        connection_args = {
        'DB_DATABASE':  '',
        'DB_USERNAME': '',
        'DB_PASSWORD': '',
        'DB_URI': '',
        'DB_PORT': ''}
    '''
    user = connection_args.get('DB_USERNAME', None)
    password = connection_args.get('DB_PASSWORD', None)
    host = connection_args.get('DB_URI', DB_URI)
    port = connection_args.get('DB_PORT', DB_PORT)

    if user is not None and password is not None:
        connection_string = f'mongodb://{user}:{password}@{host}:{port}/'
    else:
        connection_string = f'mongodb://{host}:{port}/'

    client = MongoClient(connection_string)

    return client


if __name__ == '__main__':
    client = raw_connection()
