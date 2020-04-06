'''
======================================================================
Generic wrapper for validator
----------------------------------------------------------------------
'''
import json
from importlib import import_module
from carte_blanche_utils.find_path import walk
_path = walk(keyfile='README.md', start_file=__file__)
print(_path)
from carte_blanche_utils.validators import Validator
errors = import_module('carte_blanche_utils.validators.__errors__')

fixture_path = f'{_path}/tests/validators/__fixtures__.json'

with open(fixture_path, 'r') as fin:
    fixtures = json.load(fin)
print(fixtures)
good_input = fixtures['good_input']
bad_input = fixtures['bad_input']


def test_dict_schema():

    schema = fixtures['dict_schema']

    validator = Validator(schema=schema)

    assert schema == validator.schema
    assert validator.validate(good_input) is True

    try:
        validator.validate(bad_input)
    except errors.ValidationException as exception:
        assert isinstance(exception, errors.ValidationException)


def test_file_schema():

    schema = f"{_path}/{fixtures['file_schema']}"

    validator = Validator(schema=schema)

    assert fixtures['dict_schema'] == validator.schema
    assert validator.validate(good_input) is True

    try:
        validator.validate(bad_input)
    except errors.ValidationException as exception:
        assert isinstance(exception, errors.ValidationException)


def test_bad_file_schema():
    schema = f"{_path}/{fixtures['bad_file_schema']}"

    try:
        Validator(schema=schema)
    except errors.SchemaException as exception:
        assert isinstance(exception, errors.SchemaException)


def test_missing_file_schema():
    schema = f"{_path}/{fixtures['missing_file_schema']}"

    try:
        Validator(schema=schema)
    except errors.SchemaException as exception:
        assert isinstance(exception, errors.SchemaException)
