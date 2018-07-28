'''
======================================================================
Error classses for skeleton_utils serializers
----------------------------------------------------------------------
'''


class SkeletonUtilsValidatorException(Exception):
    """docstring for SkeletonUtilsValidatorException"""
    def __init__(self):
        super(SkeletonUtilsValidatorException, self).__init__()

class SkeletonUtilsValidatorSchemaException(SkeletonUtilsValidatorException):
    """docstring for SkeletonUtilsValidatorSchemaException"""
    def __init__(self, args):
        super(SkeletonUtilsValidatorSchemaException, self).__init__()

        self.exception = {
            'title': 'SkeletonUtilsValidatorSchemaException',
            'detail': 'Invalid Schema: {0}'.format(args['exception'])
        }

class SkeletonUtilsValidatorValidationException(SkeletonUtilsValidatorException):
    """docstring for SkeletonUtilsValidatorValidationException"""
    def __init__(self, args):
        super(SkeletonUtilsValidatorValidationException, self).__init__()
        self.exception = {
            'title': 'SkeletonUtilsValidatorValidationException',
            'detail': 'An exception occurred during validation: {0}'.format(args['exception'])
        }


