'''
======================================================================
Error classses for carte blanche_utils validators
----------------------------------------------------------------------
'''


class CarteBlancheUtilsValidatorException(Exception):
    """docstring for CarteBlancheUtilsValidatorException"""
    def __init__(self):
        super(CarteBlancheUtilsValidatorException, self).__init__()

class CarteBlancheUtilsValidatorSchemaException(CarteBlancheUtilsValidatorException):
    """docstring for CarteBlancheUtilsValidatorSchemaException"""
    def __init__(self, args):
        super(CarteBlancheUtilsValidatorSchemaException, self).__init__()

        self.exception = {
            'title': 'CarteBlancheUtilsValidatorSchemaException',
            'detail': 'Invalid Schema: {0}'.format(args['exception'])
        }

class CarteBlancheUtilsValidatorValidationException(CarteBlancheUtilsValidatorException):
    """docstring for CarteBlancheUtilsValidatorValidationException"""
    def __init__(self, args):
        super(CarteBlancheUtilsValidatorValidationException, self).__init__()
        self.exception = {
            'title': 'CarteBlancheUtilsValidatorValidationException',
            'detail': 'An exception occurred during validation: {0}'.format(args['exception'])
        }


