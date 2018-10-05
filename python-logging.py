import logging
import logstash
import sys
import time


test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('18.218.123.194', 5959, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')

#add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 126,
    'test_list': [1, 2, 3],
}
test_logger.info('python-logstash: test extra fields', extra=extra)


def add(x, y):

    return x + y

def subtract(x, y):

    return x - y

def multiply(x, y):

    return x * y

def divide(x, y):
    try:
       result = x / y
    except ZeroDivisionError:
        test_logger.error('Tried to divide by zero')
    else:
        return result

def modulus(x, y):
    try:
       result = x % y
    except ZeroDivisionError:
        test_logger.warning('Denominator cannot be zero')
    else:
        return result

num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
test_logger.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
test_logger.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
test_logger.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
test_logger.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))

modulus_result = modulus(num_1, num_2)
test_logger.info('Modul: {} % {} = {}'.format(num_1, num_2, modulus_result))
