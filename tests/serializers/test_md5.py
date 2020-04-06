'''
======================================================================
Generic wrapper for md5 generator
----------------------------------------------------------------------
'''
from importlib import import_module
from carte_blanche_utils.find_path import walk
_path = walk(keyfile='README.md')

from carte_blanche_utils.serializers.md5_ import hash
errors = import_module('carte_blanche_utils.serializers.__errors__')


def test_json_list():
    DATA = [1, 2, 3]

    hashed_data = hash(DATA)

    assert isinstance(hashed_data, str)


def test_string():
    DATA = '1,2,3'

    hashed_data = hash(DATA)

    assert isinstance(hashed_data, str)


def test_byte_string():
    DATA = b'1,2,3'

    hashed_data = hash(DATA)

    assert isinstance(hashed_data, str)


def test_unicode_string():
    DATA = u'1,2,3'

    hashed_data = hash(DATA)

    assert isinstance(hashed_data, str)
