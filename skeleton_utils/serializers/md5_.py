'''
======================================================================
Generic wrapper for md5 generator
----------------------------------------------------------------------
'''
import json
from importlib import import_module
from hashlib import md5

from skeleton_utils.find_path.find_path import walk
walk()

errors = import_module('skeleton_utils.serializers.__errors__')


def hash(data):
    hasher = md5()
    try:
        string_data = json.dumps(data).encode('utf-8')
    except TypeError as type_error:
        try:
            string_data = data.decode('utf-8').encode('utf-8')
        except AttributeError as attribute_error:
            args = {'message': str(attribute_error)}

            exception = errors.SkeletonSerializerUnHashableDataTypeException(args)

            raise exception

    try:
        hasher.update(string_data)

        hashed_data = hasher.hexdigest()

        return hashed_data

    except Exception as exception:
        base_exception = errors.SkeletonSerializerException()

        raise base_exception


if __name__ == '__main__':
    JSON_DATA = [1, 2, 3]

    BYTE_DATA = b'1,2,3'
    STRING_DATA = '1,2,3'
    FILE_DATA = open('./tests/fixtures/serializers/test_file.txt')
    UNICODE_DATA = u'1,2,3'

    print(hash(UNICODE_DATA))

    print(hash(JSON_DATA))
    print(hash(BYTE_DATA))
    print(hash(STRING_DATA))
    print(hash(FILE_DATA))


