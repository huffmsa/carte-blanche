'''
======================================================================
Generic wrapper for validator
----------------------------------------------------------------------
'''
import os
import json
from importlib import import_module
from skeleton_utils.find_path import find_path
ROOT_PATH = find_path.walk().replace('/virtualenv', '')

from skeleton_utils.validators.validator import Validator
errors = import_module('skeleton_utils.validators.__errors__')

fixture_path = os.path.join(ROOT_PATH, 'tests', 'validators', '__fixtures__.json')

print(fixture_path)
with open(fixture_path, 'r') as fin:
    fixtures = json.load(fin)

good_input = fixtures['good_input']
bad_input = fixtures['bad_input']


def test_dict_schema():

    schema = fixtures['dict_schema']

    validator = Validator()
    validator.schema(schema)

    assert schema == validator.schema_
    assert validator.validate(good_input) == True

    try:
        validator.validate(bad_input)
    except errors.SkeletonUtilsValidatorValidationException as exception:
        assert isinstance(exception, errors.SkeletonUtilsValidatorValidationException)


def test_file_schema():

    schema = fixtures['file_schema']

    validator = Validator()
    validator.schema(schema)

    assert fixtures['dict_schema'] == validator.schema_
    assert validator.validate(good_input) == True

    try:
        validator.validate(bad_input)
    except errors.SkeletonUtilsValidatorValidationException as exception:
        assert isinstance(exception, errors.SkeletonUtilsValidatorValidationException)


def test_bad_file_schema():
    schema = fixtures['bad_file_schema']

    validator = Validator()
    try:
        validator.schema(schema)
    except errors.SkeletonUtilsValidatorSchemaException as exception:
        assert isinstance(exception, errors.SkeletonUtilsValidatorSchemaException)


def test_missing_file_schema():
    schema = fixtures['missing_file_schema']

    validator = Validator()
    try:
        validator.schema(schema)
    except errors.SkeletonUtilsValidatorSchemaException as exception:
        assert isinstance(exception, errors.SkeletonUtilsValidatorSchemaException)
