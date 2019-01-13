'''
======================================================================
Generic wrapper for different validators
----------------------------------------------------------------------
'''
import json
import jsonschema
from importlib import import_module

from carte_blanche_utils.find_path.find_path import walk
walk()

errors = import_module('carte_blanche_utils.validators.__errors__')


class Validator(object):
    """docstring for Validator"""
    def __init__(self):
        super(Validator, self).__init__()
        self.schema_ = {}
        self.validate_= self.validate


    def schema(self, schema_path):

        if isinstance(schema_path, str):

            try:
                with open(schema_path) as sp:
                    self.schema_ = json.load(sp)
            except Exception as exception:

                vaildator_exception = errors.CarteBlancheUtilsValidatorSchemaException({'exception': exception})

                raise vaildator_exception
        elif isinstance(schema_path, dict):

            self.schema_ = schema_path


    def validate(self, input):

        try:
            jsonschema.validate(input, self.schema_)
            return True

        except jsonschema.exceptions.ValidationError as validation_error:
            ve_string = str(validation_error.message)
            # print(ve_string)

            vaildator_exception = errors.CarteBlancheUtilsValidatorValidationException({'exception': ve_string})



            raise vaildator_exception



if __name__ == '__main__':
    validator = Validator()

    print(validator)

    schema_path = {
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            }
        },
        "additionalProperties": False
    }

    validator.schema(schema_path)

    input_ = {'name': 'foo', 'key': 'bar'}

    try:
        print(validator.validate(input_))
    except errors.CarteBlancheUtilsValidatorValidationException as exception:
        print(exception.exception)
