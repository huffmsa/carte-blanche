'''
======================================================================
Generic wrapper for md5 generator
----------------------------------------------------------------------
'''
import os
import json
from importlib import import_module
from carte_blanche_utils.find_path import find_path
ROOT_PATH = find_path.walk().replace('/virtualenv', '')

from carte_blanche_utils.serializers.sha_ import hash
from carte_blanche_utils.serializers.salt import create
errors = import_module('carte_blanche_utils.serializers.__errors__')

fixture_path = os.path.join(ROOT_PATH, 'tests', 'serializers', '__fixtures__.json')
print(fixture_path)
with open(fixture_path, 'r') as fin:
    fixtures = json.load(fin)


def test_json_list():
    DATA = [1, 2, 3]
    SALT = create()
    ARGS = {
        "data": DATA,
        "salt": SALT
    }

    hashed_data, hashed_salt = hash(ARGS)

    assert isinstance(hashed_data, str)
    assert hashed_data == fixtures['test_sha']['test_array']['hashed_data']


def test_string():
    DATA = '1,2,3'
    SALT = create()
    ARGS = {
        "data": DATA,
        "salt": SALT
    }
    hashed_data, hashed_salt = hash(ARGS)

    assert isinstance(hashed_data, str)
    assert hashed_data == fixtures['test_sha']['test_string']['hashed_data']


def test_byte_string():
    DATA = b'1,2,3'
    SALT = create()
    ARGS = {
        "data": DATA,
        "salt": SALT
    }
    hashed_data, hashed_salt = hash(ARGS)

    assert isinstance(hashed_data, str)
    assert hashed_data == fixtures['test_sha']['test_byte_string']['hashed_data']


def test_unicode_string():
    DATA = u'1,2,3'
    SALT = create()
    ARGS = {
        "data": DATA,
        "salt": SALT
    }
    hashed_data, hashed_salt = hash(ARGS)

    assert isinstance(hashed_data, str)
    assert hashed_data == fixtures['test_sha']['test_unicode_string']['hashed_data']


def test_file_data_array():
    DATA = open('./tests/fixtures/serializers/test_file.txt')
    SALT = create()
    ARGS = {
        "data": DATA,
        "salt": SALT
    }
    try:
        hashed_data, hashed_salt = hash(ARGS)
    except errors.CarteBlancheSerializerUnHashableDataTypeException as exception:

        assert exception.code == 1001
