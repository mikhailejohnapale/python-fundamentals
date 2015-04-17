# 33-regular-expressions.py
import re

v = [
    'git 0.1.2',
    'ruby 0.23',
    'python 3.1.3'
]

for e in v:
    if re.search(r'[0-9]*\.[0-9]*\.[0-9]*|[0-9]*\.[0-9]*', e):
        print(e, 'MATCH!')
    else:
        print(e, 'NO MATCH!')
