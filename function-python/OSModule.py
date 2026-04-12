# underlying operating system

import os 
from datetime import datetime
#print(dir(os)) #It shows all functions, variables, and attributes inside the os module
#print(os.getcwd())   # current directory

os.chdir('/Users/techysanoj/Desktop/function-python')  #changes current working folder

 
#os.mkdir('demo.txt-2/Sub-Dir-1')
#os.makedirs('demo.txt-2')
#'demo.txt-2'
#os.rmdir('demo.txt-2/Sub-Dir-1')
#os.removedirs('demo.txt-2  /Sub-Dir-1')
#os.rmdir('demo.txt-2')
#os.rename('oop.py','OOPS.py')
#print(os.getcwd())
# print(os.stat('OOPS.py').st_size)
# mod_time = os.stat('OOPS.py').st-mtime
# print(datetime.fromtimestamp(mod_time))
# #print(os.listdir())   

# for dirpath, dirnames, filenames in os.walk('Users/techysanoj/Desktop/function-python/'):
#     print('Current path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:',filenames) 
#     print()

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'practice.txt')
print(file_path )
print(os.path.basename('/tmp/demo.txt'))
print(os.path.split('/tmp/demo.txt'))
print(os.path.dirname('/tmp/demo.txt'))
print(os.path.exists('/tmp/demo.txt'))
print(os.path.isdir('/tmp/demo.txt'))
print(os.path.isfile('/tmp/demo.txt'))
print(os.path.splitext('/tmp/demo.txt'))
print(dir(os.path))