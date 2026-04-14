first_name = 'Supriya '
last_name = 'Kumari'

#sentence = 'My name is {} {}'.format (first_name, last_name)
#print(sentence) #older version '.format() {} → placeholders
#.format(first_name, last_name) → fills values in order

#sentence = f'My name is {first_name} {last_name}' #No need to match order like .format()->directly write variable inside {}
#print(sentence) #simple  no need  to check in which placholder which need to add

#sentence = f'My name is {first_name.upper()} {last_name.upper()}'
#print(sentence)

#Using formatting methods

person = {'name': 'Supriya', 'age': 23}

# sentence = 'My name is {} and I am {} years old' .format(person['name'],person['age'])
# print(sentence)



calculation = f"4 times 11 is equal to {4*11}"
print(calculation)

for n in range(1,11):
     sentence = f'The value is {n:02}' #always show 2 digits Adds leading zero if needed
     print(sentence)

pi = 3.14159265
sentence = f'Pi is equal to {pi:.4f}'
print(sentence)

from datetime import datetime

birthday = datetime(2001,11,6)

sentence = f'Supriya has a birthday on {birthday:%B %d, %Y}'
print(sentence)