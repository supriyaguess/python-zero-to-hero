'''LEGB

Local, Enclosing, Global, Built_int
'''
# x = 'global x'

# def test():
# global x
 # x  = 'local x'
#     y = 'local y'  #local variable and it is local to this test function 
#      # print(y)
#     print(x)

# test()
# #print(y) guves error
# print(x)

# x = 10 # global variable

# def my_function():
#     global x
#     x = 4
#     y = 5 # local variable
#     print(y)

# my_function()
# print(x)
# #print(y) # gives error bcoz y is a local variables and is not accessible outside os the function

# import builtins
# print(dir(builtins))

# m = min([5,1,4,2,3])
# print(m)

def outer():
    x = 'outer x'

    def inner():
        # x = 'inner x'

        print(x)

    inner()
    print(x)

outer()