'''
======================================================================
Error classses for skeleton_utils serializers
----------------------------------------------------------------------
'''


class SkeletonSerializerException(Exception):
    """docstring for SkeletonSerializerException"""
    def __init__(self):
        super(SkeletonSerializerException, self).__init__()
        self.code = 1000
        self.exception = {
            'code': self.code,
            'title': 'SkeletonSerializerException',
            'message': 'Base Exception for the Skeleton serializers. You fucked up'
        }


class SkeletonSerializerUnHashableDataTypeException(SkeletonSerializerException):
    """docstring for SkeletonSerializerUnHashableDataTypeException"""
    def __init__(self, args):
        super(SkeletonSerializerUnHashableDataTypeException, self).__init__()
        self.args = args
        self.code = 1001
        self.exception = {
            'code': self.code,
            'title': 'SkeletonSerializerUnHashableDataTypeException',
            'message': '{0} is not currently supported by this serializer'
                        .format(args['message']),
            'detail': args['message']
        }
