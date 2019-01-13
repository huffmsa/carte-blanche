'''
======================================================================
Generic wrapper for sha256 generator
----------------------------------------------------------------------
'''
import json
from importlib import import_module
from hashlib import sha256
import hmac

from carte_blanche_utils.find_path.find_path import walk
walk()

errors = import_module('carte_blanche_utils.serializers.__errors__')


def hash(args):

    try:
        salt = json.dumps(args['salt']).encode('utf-8')
    except TypeError as type_error:
        salt = args['salt'].decode('utf-8').encode('utf-8')
        try:
            salt = args['salt'].decode('utf-8').encode('utf-8')

        except AttributeError as attribute_error:
            exception_args = {'message': str(attribute_error)}

            exception = errors.CarteBlancheSerializerUnHashableDataTypeException(exception_args)

            raise exception

    try:
        string_data = json.dumps(args['data']).encode('utf-8')
    except TypeError as type_error:
        try:
            string_data = args['data'].decode('utf-8').encode('utf-8')

        except AttributeError as attribute_error:
            exception_args = {'message': str(attribute_error)}

            exception = errors.CarteBlancheSerializerUnHashableDataTypeException(exception_args)

            raise exception

    try:
        hasher = hmac.new(string_data, digestmod=sha256)
        hashed_data = hasher.hexdigest()
        hasher.update(salt)

        hashed_salt = hasher.hexdigest()

        return hashed_data, hashed_salt

    except Exception as exception:
        base_exception = errors.CarteBlancheSerializerException()

        raise base_exception


if __name__ == '__main__':
    from carte_blanche_utils.serializers.salt import create
    SALT = create()
    JSON_DATA = [1, 2, 3]

    BYTE_DATA = b'1,2,3'
    STRING_DATA = '1,2,3'
    FILE_DATA = open('./tests/fixtures/serializers/test_file.txt')
    UNICODE_DATA = u'1,2,3'

    print(hash({'salt': SALT, 'data': JSON_DATA}))
    print(hash({'salt': SALT, 'data': STRING_DATA}))
    print(hash({'salt': SALT, 'data': BYTE_DATA}))
    print(hash({'salt': SALT, 'data': UNICODE_DATA}))

    try:
        print(hash({'salt': SALT, 'data': FILE_DATA}))
    except errors.CarteBlancheSerializerUnHashableDataTypeException as exception:
        print(exception.exception)
