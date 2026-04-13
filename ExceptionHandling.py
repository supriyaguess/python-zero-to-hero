

try:
    #f = open('testfile.txt') [Errno 2] No such file or directory: 'testfile.txt'
   f = open('test_file.txt')
   # var = bad_var. error:name 'bad_var' is not defined
#except Exception: # this is to general so it will run in everycase
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:  #else clause only runs when it dont through any error
    print(f.read()) #return Test File Contentss!
    f.close
finally:   # always runs no matter what hapenend weather code is succesfull or not 
    print("Executing Finally...")


try:
    f = open('currupt_file.txt')
    if f.name == 'currupt_file.txt':
        raise Exception
except FileExistsError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finaly...")