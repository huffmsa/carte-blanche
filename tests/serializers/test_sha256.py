'''
======================================================================
Generic wrapper for md5 generator
----------------------------------------------------------------------
'''
from carte_blanche_utils.find_path import walk
walk()
from carte_blanche_utils.serializers.sha_ import hash


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

