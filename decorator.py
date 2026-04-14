# def outer_func():
#     message = 'Hi'

#     def inner_func():
#         print(message)
#     return inner_func

# my_func = outer_func()
# my_func()
# my_func()
# my_func()

# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)
#     return inner_func

# hi_func = outer_func('Hi')
# by_func = outer_func('Bye')

# hi_func()
# by_func()

def outer_func(msg):

    def inner_func():
        print(msg)
    return inner_func

hi_func = outer_func('Hi')
by_func = outer_func('Bye')

hi_func()
by_func()

#Decorator is a function that takes another function as input, adds extra functionality,
#  and returns a new function.
#A decorator wraps a function to extend its behavior without modifying its code.

def decorator_func(original_func):

    def wrapper(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_func.__name__))
        original_func(*args, **kwargs) # they allows to us any artibitary number
        print("After function")

    return wrapper

class decorator_class(object):

    def __init__(self,original_func):
        self.original_func = original_func
    def __call__(self, *args, **kwds):
        print('call method executed this before {}'.format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)
# @decorator_func
# def display():
#     print("Display function ran")

# @decorator_func
# def display_info(name,age):
#     print('display_info ran with arguments ({}, {})'.format(name,age))

# display_info('Supriya',23)

# display()

#display = decorator_func(display) same to same @decorator_func


# Practical Examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time

# @decorator_func
# def display():
#     print("Display function ran")

@my_timer
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))


@my_logger
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name,age))

@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name,age))


display_info('Sanoj',30)

# display()
