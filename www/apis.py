# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
JSON API
'''

import json, logging, inspect, functools

class APIError(Exception):
    '''
    the base APIError which contains error(request),data(operationl),and message(optional)
    '''
    def __init__(self, error, data='', message=''):
        super(APIError,self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid, The data specfies the error field of input from
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found., The data specfies the reource name
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission
    '''
    def __init__(self, field, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)