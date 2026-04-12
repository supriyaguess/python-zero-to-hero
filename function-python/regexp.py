import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

Supriya.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'


patt = re.compile(r'abc')
mat = patt.finditer(text_to_search)
for matc in mat:
    print(matc)
patt = re.compile(r'.')
patt = re.compile(r'Supriya \.com')
mat = patt.finditer(text_to_search)
for matc in mat:
    print(matc)
pattern = re.compile(r'start', re.I)
print('\tTab') # it will leave space ---Tab
print(r'\tTab') # it will return exact

matches = pattern.search(sentence)

print(matches)