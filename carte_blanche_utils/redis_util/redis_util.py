import os
import redis

'''
======================================================================
Connection utilities for redis
----------------------------------------------------------------------
'''

REDIS_DB_URI = os.environ.get('REDIS_DB_URI', 'localhost')
REDIS_DB_PORT = os.environ.get('REDIS_DB_PORT', '6379')
REDIS_DB_DATABASE = int(os.environ.get('REDIS_DB_DATABASE', '0'))


def connect(connection_args={}):
    '''
        connection_args = {
            'db_uri': '',
            'db_port': '',
            'db_database': ''
        }
    '''
    db_uri = connection_args.get('db_uri', REDIS_DB_URI)
    port = connection_args.get('db_port', REDIS_DB_PORT)
    database = connection_args.get('db_database', REDIS_DB_DATABASE)

    redis_db = redis.Redis(host=db_uri, port=port, db=database, socket_connect_timeout=3)

    return redis_db
